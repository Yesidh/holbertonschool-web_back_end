#!/usr/bin/python3
"""
===============================================================================
a class FIFOCache that inherits from BaseCaching and is a caching system:

You must use self.cache_data - dictionary from the parent class BaseCaching
You can overload def __init__(self): but don’t forget to call the parent
 init: super().__init__()
def put(self, key, item):
Must assign to the dictionary self.cache_data the item value for the key key.
If key or item is None, this method should not do anything.
If the number of items in self.cache_data is higher that BaseCaching.MAX_ITEMS:
you must discard the first item put in cache (FIFO algorithm)
you must print DISCARD: with the key discarded and following by a new line
def get(self, key):
Must return the value in self.cache_data linked to key.
If key is None or if the key doesn’t exist in self.cache_data, return None.
===============================================================================
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
        class that inherits from BaseCaching
    """

    def __init__(self):
        """
            starting with parent class
        """
        super().__init__()

    def put(self, key, item):
        """
        :param key: key to add into cache_data dictionary
        :param item: valeu for a key
        :return: anything, only adding data to cache_data
        """
        if key is not None and item is not None and BaseCaching.MAX_ITEMS:
            if self.cache_data.get(key) is None:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    key_to_del = list(self.cache_data.keys())[0]
                    del self.cache_data[key_to_del]
                    print("DISCARD: {}".format(key_to_del))
            if len(self.cache_data) <= BaseCaching.MAX_ITEMS:
                self.cache_data[key] = item

    def get(self, key):
        """
            :param key: value to get from the dictionary cache_data
            :return:
        """
        if key is None or self.cache_data.get(key) is None:
            return None
        else:
            return self.cache_data.get(key)
