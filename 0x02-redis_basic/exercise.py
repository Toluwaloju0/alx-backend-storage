#!/usr/bin/env python3
"""A module to create a redis cache"""

from functools import wraps
import redis
from typing import Any, Callable


# def count_calls(method: Callable) -> Callable:
#     @wraps(method)

class Cache:
    """A class for the redis database"""

    def __init__(self):
        self._redis = redis.Redis()

        self._redis.flushdb()

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
                print(data)
                return data
        else:
            print(data)
            return data
