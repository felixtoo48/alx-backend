#!/usr/bin/env python3
""" FIFO cathing method/ caching system"""


BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ FIFO caching system class definition """
    def __init__(self):
        """ initializing the class and parent class """
        super().__init__()

    def put(self, key, item):
        """ assigns to the dictionary self.cache_data
        the item value for the key 'key'
        if number of items is higher than 'MAX_ITEMS'
        then remove the first in cache
        """
        if len(self.cache_data) >= self.MAX_ITEMS:
            self.remove_oldest()
            print ("DISCARD:" {oldest(key)})

        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ returns the value in the dictionary 'self.cache_data'
        linked to 'key' """
        if key is None:
            return None

        return self.cache_data.get(key)
