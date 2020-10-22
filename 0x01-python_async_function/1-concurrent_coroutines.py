#!/usr/bin/env python3
"""
===============================================================================
Import wait_random from the previous python file that you’ve written and write
an async routine called wait_n that takes in 2 int arguments
(in this order): n and max_delay. You will spawn wait_random n times with the
specified max_delay.
wait_n should return the list of all the delays (float values). The list of
the delays should be in ascending order without using sort() because of
concurrency.
===============================================================================
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int = 0, max_delay: int = 10) -> List[float]:
    """
        :param n: times to call wait_random function
        :param max_delay: maximum delay in each wait_random call
        :return: a sorting list whit float values
    """
    list_float_random_values: List[float] = []
    list_float: List = []
    for _ in range(n):
        list_float.append(wait_random(max_delay))

    for value in asyncio.as_completed(list_float):
        delay = await value
        list_float_random_values.append(delay)

    return list_float_random_values
