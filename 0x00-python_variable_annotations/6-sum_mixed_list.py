#!/usr/bin/env python3
"""
===============================================================================
a type-annotated function sum_mixed_list which takes a list mxd_lst of integers
and floats and returns their sum as a float.
===============================================================================
"""
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """
        :param mxd_list: list with int and float values
        :return: the list sum
    """
    return sum(mxd_list)
