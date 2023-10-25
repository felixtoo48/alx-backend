#!/usr/bin/env python3
""" BasicCache class inheriting from BaseCaching"""


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache class inheriting from BaseCaching
    my Cache
    """

    def put(self, key, item):
        """ assigns to the dictionary self.cache_data
        the item value for the key 'key'"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ returns the value in the dictionary 'self.cache_data'
        linked to 'key' """
        if key is None:
            return None

        return self.cache_data.get(key)
