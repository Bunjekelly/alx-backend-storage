#!/usr/bin/env python3

"""a Cache class"""

import redis
import uuid


class Cache:
    def __init__(self):
        """initialization"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: str or bytes or int or float) -> str:
        """takes a data argument and returns a string"""
        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)
        return random_key
