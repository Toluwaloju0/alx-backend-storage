#!/usr/bin/env python3
"""A module to create a redis cache"""

from functools import wraps
import redis
from typing import Any, Callable, List, Union


def count_calls(method: Callable) -> Callable:
    """A wrapper to wrap a function and count it calls"""

    @wraps(method)
    def wrapper(*args, **kwargs):
        """A function to process a method and return it"""

        result = method(*args)
        self = args[0]
        self._redis.incr(f"{method.__qualname__}")
        return result
    return wrapper


def call_history(method: Callable) -> Callable:
    """A wrapper to store inputs and outputs in a list"""

    @wraps(method)
    def wrapper_list(*args, **kwargs):
        """A function to push values into a redis list"""

        key_input = f"{method.__qualname__}:inputs"
        key_output = f"{method.__qualname__}:outputs"

        self = args[0]
        new_tuple = (args[1],)
        self._redis.rpush(key_input, f"{new_tuple}")
        result = method(*args)
        self._redis.rpush(key_output, result)

        return result
    return wrapper_list


class Cache:
    """A class for the redis database"""

    def __init__(self):
        self._redis = redis.Redis()

        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """A function to store into a redis database"""

        import uuid

        id = str(uuid.uuid4())
        self._redis.set(id, data)

        return id

    def get(self, key: str, fn: Callable = None):
        """A function to get and convert data from redis"""

        data = self._redis.get(key)

        if data and fn:
            data = fn(data)
        return data

    def get_int(self, key: str):
        """A function to get a int data"""

        data = self._redis.get(key)
        print(data, '-----', key)
        try:
            data = int(data)
            return data
        except Exception:
            return None

    def get_str(self, key: str):
        try:
            data = self._redis.get(key)
            return data.decode('utf-8')
        except Exception:
            return None


def replay(method: callable):
    """A function to get the inputs in adatabase"""

    r = redis.Redis()

    print(f'{method.__qualname__} was \
called {int(r.get(method.__qualname__))} times:')

    key_input = f"{method.__qualname__}:inputs"
    key_output = f"{method.__qualname__}:outputs"

    items = zip(
        r.lrange(key_input, 0, -1),
        r.lrange(key_output, 0, -1)
    )

    for item in items:
        print(f"{method.__qualname__} {item[0].decode('utf-8')} -> {item[1]}")
