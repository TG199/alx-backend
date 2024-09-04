#!/usr/bin/env python3
""" Fifo Caching module
"""


class BaseCaching():
    """ BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    MAX_ITEMS = 4

    def __init__(self):
        """ Initiliaze
        """
        self.cache_data = {}

    def print_cache(self):
        """ Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """ Add an item in the cache
        """
        raise NotImplementedError(
            "put must be implemented in your cache class"
            )

    def get(self, key):
        """ Get an item by key
        """
        raise NotImplementedError(
            "get must be implemented in your cache class"
            )


class FIFOCache(BaseCaching):
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        if key is None or item is None:
            pass
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            first_key = next(iter(self.cache_data))
            print(f"DISCARD: {first_key}")
            self.cache_data.pop(first_key)
        self.cache_data[key] = item

    def get(self, key):
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
