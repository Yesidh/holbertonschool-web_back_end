#!/usr/bin/env python3
"""
===============================================================================
a type-annotated function make_multiplier that takes a float multiplier as
argument and returns a function that multiplies a float by multiplier.
===============================================================================
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
        :param multiplier:
        :return: a function that multiplies two values
    """

    def multiply(f: float) -> float:
        """
        :param f: float value
        :return: f * multiplier
        """
        return f * multiplier

    return multiply
