#!/usr/bin/env python3
""" MRU Caching module that inherits from BaseCaching
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
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
            mru = list(self.cache_data.keys())[-1]
            print(f"DISCARD: {mru}")
            self.cache_data.pop(mru)
        self.cache_data[key] = item

    def get(self, key):
        """
        Get cache from cache system
        """
        if key is None or key not in self.cache_data.keys():
            return None
        mru = self.cache_data.pop(key)
        self.cache_data[key] = mru
        return self.cache_data[key]
