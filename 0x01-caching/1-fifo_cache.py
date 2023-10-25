#!/usr/bin/env python3
""" FIFO cathing method/ caching system"""


BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ FIFO caching system class definition """
    def __init__(self):
        """ initializing the class and parent class """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ assigns to the dictionary self.cache_data
        the item value for the key 'key'
        if number of items is higher than 'MAX_ITEMS'
        then remove the first in cache
        """
        if len(self.cache_data) >= self.MAX_ITEMS:
            oldest_key = self.order[0]
            print(f"DISCARD: {self.order[0]}")
            self.remove_oldest(oldest_key)

        if key is not None and item is not None:
            self.cache_data[key] = item
            self.order.append(key)

    def remove_oldest(self, key):
        self.order.remove(key)  # Remove the key from the order list
        del self.cache_data[key]

    def get(self, key):
        """ returns the value in the dictionary 'self.cache_data'
        linked to 'key' """
        if key is None:
            return None

        return self.cache_data.get(key)
