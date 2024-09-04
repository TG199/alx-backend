#!/usr/bin/env python3
""" Lifo Caching module that inherits from BaseCaching
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFO cache class
    """

    def __init__(self):
        """
        Instantiation
        """
        super().__init__()

    def put(self, key, item):
        """
        Put cache on cache system
        """
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last_key = list(self.cache_data.keys())[-1]
            print(f"DISCARD: {last_key}")
            self.cache_data.pop(last_key)
        self.cache_data[key] = item

    def get(self, key):
        """
        Get cache from cache system
        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
