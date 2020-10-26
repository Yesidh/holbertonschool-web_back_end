#!/usr/bin/python3
"""
===============================================================================
Create a class BasicCache that inherits from BaseCaching and is a caching
system:

You must use self.cache_data - dictionary from the parent class BaseCaching
This caching system doesn’t have limit
def put(self, key, item):
Must assign to the dictionary self.cache_data the item value for the key key.
If key or item is None, this method should not do anything.
def get(self, key):
Must return the value in self.cache_data linked to key.
If key is None or if the key doesn’t exist in self.cache_data, return None.
===============================================================================
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
        inherit from BaseCaching to overwrite functions
    """
    def put(self, key, item):
        """
            :param key: key value
            :param item: item value
            :return: anything, add pair key, value to dictionary cache_data
        """
        if key or item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
            :param key: value to get from the dictionary cache_data
            :return:
        """
        return self.cache_data.get(key)
