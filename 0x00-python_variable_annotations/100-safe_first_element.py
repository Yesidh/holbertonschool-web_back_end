#!/usr/bin/env python3
"""
===============================================================================
Augment the following code with the correct duck-typed annotations:

# The types of the elements of the input are not know
def safe_first_element(lst):
    if lst:
        return lst[0]
    else:
        return None
===============================================================================
"""

from typing import Any, Union, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
        :param lst: sequence of any type elements
        :return: Union of any an none type elements
    """
    if lst:
        return lst[0]
    else:
        return None
