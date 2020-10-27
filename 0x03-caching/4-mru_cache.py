#!/usr/bin/python3
"""
===============================================================================
a class MRUCache that inherits from BaseCaching and is a caching system:

You must use self.cache_data - dictionary from the parent class BaseCaching
You can overload def __init__(self): but don’t forget to call the parent
 init: super().__init__()

def put(self, key, item):
Must assign to the dictionary self.cache_data the item value for the key key.
If key or item is None, this method should not do anything.
If the number of items in self.cache_data is higher that BaseCaching.MAX_ITEMS:
you must discard the most recently used item (MRU algorithm)
you must print DISCARD: with the key discarded and following by a new line
def get(self, key):
Must return the value in self.cache_data linked to key.
If key is None or if the key doesn’t exist in self.cache_data, return None.
===============================================================================
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
        LIFOCache class inherit from BaseCaching
    """

    def put(self, key, item):
        """
            :param key: key value to add/del into cache_data dictionary
            :param item: value for key
            :return: anything, only modified cache_data dictionary
        """

        if key is None or item is None:
            pass
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                key_list = list(self.cache_data.keys())
                key_to_del = key_list[len(key_list) - 1]
                if key in self.cache_data.keys():
                    del self.cache_data[key]
                else:
                    del self.cache_data[key_to_del]
                    print("DISCARD: {}".format(key_to_del))

            self.cache_data[key] = item

    def get(self, key):
        """
            :param key: value to get from the dictionary cache_data
            :return: key: value data
        """
        if key is None or self.cache_data.get(key) is None:
            return None
        else:
            value = self.cache_data[key]
            if key in self.cache_data.keys():
                del self.cache_data[key]
            self.cache_data[key] = value
            return self.cache_data.get(key)
