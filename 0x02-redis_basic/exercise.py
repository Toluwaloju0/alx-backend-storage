#!/usr/bin/env python3
"""A module to create a redis cache"""

from functools import wraps
import redis
from typing import Any, Callable


method_count = {}


def count_calls(method: Callable) -> Callable:
    @wraps(method)
    def wrapper(*args, **kwargs):
        """A function to process a method and return it"""
        if method_count.get(method.__qualname__):
            method_count[method.__qualname__] += 1
        else:
            method_count[method.__qualname__] = 1
        result = method(args[0], args[1], key=method.__qualname__)
        return result
    return wrapper


class Cache:
    """A class for the redis database"""

    def __init__(self):
        self._redis = redis.Redis()

        self._redis.flushdb()

    @count_calls
    def store(self, data: Any, key=None) -> str:
        """A function to store into a redis database"""

        if not key:
            import uuid

            id = str(uuid.uuid4())

            self._redis.set(id, data)

            return id
        else:
            self._redis.set(key, data)

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
