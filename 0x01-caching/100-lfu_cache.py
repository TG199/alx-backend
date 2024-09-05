#!/usr/bin/env python3
""" LFU Caching module that inherits from BaseCaching
"""
from base_caching import BaseCaching
from collections import defaultdict


class LFUCache(BaseCaching):
    """
    LFU Caching algorithm implementation
    """
    def __init__(self):
        """Initialize the LFU cache
        """
        super().__init__()
        self.frequency_map = defaultdict(list)
        self.key_freq = {}
        self.min_freq = 0

    def put(self, key, item):
        """Add an item in the cache
        """
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_data[key] = item
            self._update_frequency(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                self._evict_lfu()
            self.cache_data[key] = item
            self.key_freq[key] = 1
            self.frequency_map[1].append(key)
            self.min_freq = 1

    def get(self, key):
        """Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        self._update_frequency(key)
        return self.cache_data[key]

    def _update_frequency(self, key):
        """Update the frequency of an accessed key
        """
        freq = self.key_freq[key]
        self.frequency_map[freq].remove(key)
        if not self.frequency_map[freq]:
            del self.frequency_map[freq]
            if freq == self.min_freq:
                self.min_freq += 1

        self.key_freq[key] += 1
        new_freq = self.key_freq[key]
        self.frequency_map[new_freq].append(key)

    def _evict_lfu(self):
        """Evict the least frequently used item (if tie, use LRU)
        """
        lfu_keys = self.frequency_map[self.min_freq]
        evict_key = lfu_keys.pop(0)

        if not lfu_keys:
            del self.frequency_map[self.min_freq]

        del self.cache_data[evict_key]
        del self.key_freq[evict_key]

        print(f"DISCARD: {evict_key}")
