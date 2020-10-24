#!/usr/bin/env python3
"""
===============================================================================
 a type-annotated function sum_list which takes a list input_list of floats as
 argument and returns their sum as a float.
===============================================================================
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    :param input_list: list with float elements
    :return: the sum of its elements
    """
    return sum(input_list)
