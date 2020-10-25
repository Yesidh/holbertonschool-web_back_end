#!/usr/bin/env python3
"""
===============================================================================
Given the parameters and the return values, add type annotations to the
function

Hint: look into TypeVar

def safely_get_value(dct, key, default = None):
    if key in dct:
        return dct[key]
    else:
        return default
===============================================================================
"""

from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) \
        -> Union[Any, T]:
    """
    :param dct: dictionary like a object dont mutable
    :param key: any value
    :param default: Unios with tipe var
    :return: typevar
    """
    if key in dct:
        return dct[key]
    else:
        return default
