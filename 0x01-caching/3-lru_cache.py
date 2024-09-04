#!/usr/bin/env python3
""" LRU Caching module that inherits from BaseCaching
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
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
            lru = list(self.cache_data.keys())[0]
            print(f"DISCARD: {lru}")
            self.cache_data.pop(lru)
        self.cache_data[key] = item

    def get(self, key):
        """
        Get cache from cache system
        """
        if key is None or key not in self.cache_data.keys():
            return None
        value = self.cache_data.pop(key)
        self.cache_data[key] = value
        return self.cache_data[key]
