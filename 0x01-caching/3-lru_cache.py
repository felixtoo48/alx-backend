#!/usr/bin/env python3
""" LRUCache cathing method/ caching system"""
from collections import OrderedDict


BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache caching system class definition """
    def __init__(self):
        """ initializing the class and parent class """
        super().__init__()
        self.order = []
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ assigns to the dictionary self.cache_data
        the item value for the key 'key'
        if number of items is higher than 'MAX_ITEMS'
        then remove the last recently used item in cache
        """
        if key in self.cache_data:
            self.cache_data.move_to_end(key)

        elif len(self.cache_data) >= self.MAX_ITEMS:
            discard = self.cache_data.popitem(last=False)
            del self.cache_data[discard]
            print(f"DISCARD: {discard}")

        if key is not None and item is not None:
            self.order.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """ returns the value in the dictionary 'self.cache_data'
        linked to 'key' """
        if key is None:
            return None

        return self.cache_data.get(key)
