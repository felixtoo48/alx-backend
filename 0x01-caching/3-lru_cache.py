#!/usr/bin/env python3
""" LRU cathing method/ caching system"""


BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ LRU caching system class definition """
    def __init__(self):
        """ initializing the class and parent class """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ assigns to the dictionary self.cache_data
        the item value for the key 'key'
        if number of items is higher than 'MAX_ITEMS'
        then remove the least recently used item in cache
        """
        if len(self.cache_data) >= self.MAX_ITEMS:
            discard = self.order.pop(0)
            del self.cache_data[discard]
            print(f"DISCARD: {discard}")

        if key is not None and item is not None:
            if key in self.cache_data:
                # remove from order
                self.order.remove(key)
            # enque
            self.order.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """ returns the value in the dictionary 'self.cache_data'
        linked to 'key' """
        if key is None:
            return None

        # Remove from any position in the queue and add to the back
        # self.order.remove(key)
        # self.order.append(key)

        return self.cache_data.get(key)
