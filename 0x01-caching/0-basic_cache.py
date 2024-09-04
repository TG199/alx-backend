#!/usr/bin/env python3
""" BaseCache module thats inherits from BaseCaching
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Basic caching algorithm
    """

    def __init__(self):
        """Instantiation"""
        super().__init__()

    def put(self, key, item):
        """
        Put items on caching system
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Get items from caching system
        """
        try:
            return self.cache_data[key]
        except Exception:
            pass
