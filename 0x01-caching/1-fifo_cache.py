#!/usr/bin/env python3
""" Fifo Caching module that inherits from BaseCaching
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFO cache class
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
            first_key = next(iter(self.cache_data))
            print(f"DISCARD: {first_key}")
            self.cache_data.pop(first_key)
        self.cache_data[key] = item

    def get(self, key):
        """
        Get cache from cache system
        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
