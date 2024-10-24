#!/usr/bin/env python3
"""A module to create a redis cache"""

from functools import wraps
import redis
from typing import Any, Callable


def count_calls(method: Callable) -> Callable:
    @wraps(method)
    def wrapper(*args, **kwargs):
        """A function to process a method and return it"""

        r = redis.Redis()
        r.incr(method.__qualname__)
        result = method(*args)
        return result
    return wrapper


def call_history(method: Callable) -> Callable:
    @wraps(method)
    def wrapper_list(*args, **kwargs):i
        """A function to push values into a redis list"""

        key_input = f"{method.__qualname__}:inputs"
        key_output = f"{method.__qualname__}:outputs"
        
        r = redis.Redis()
        r.rpush(key_input, str(args[1]))
        result = method(*args)
        r.rpush(key_output, result)

        return result
    return wrapper_list


class Cache:
    """A class for the redis database"""

    def __init__(self):
        self._redis = redis.Redis()

        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Any) -> str:
        """A function to store into a redis database"""

        import uuid

        id = str(uuid.uuid4())
        self._redis.set(id, data)

        return id

    def get(self, key: str, fn: Callable = None):
        """A function to get and convert data from redis"""

        data = self._redis.get(key)

        if data and fn:
            try:
                data = fn(data)
            except Exception:
                pass
            finally:
                return data
        else:
            return data
