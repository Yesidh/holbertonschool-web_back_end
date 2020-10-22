#!/usr/bin/env python3
"""
===============================================================================
Take the code from wait_n and alter it into a new function task_wait_n.
The code is nearly identical to wait_n except task_wait_random is being called.
===============================================================================
"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').wait_random


async def task_wait_n(n: int = 0, max_delay: int = 10) -> List[float]:
    """
        :param n: times to call wait_random function
        :param max_delay: maximum delay in each wait_random call
        :return: a sorting list whit float values
    """
    list_float_random_values: List[float] = []
    list_float: List[asyncio.Task] = []

    for _ in range(n):
        list_float.append(task_wait_random(max_delay))

    for value in asyncio.as_completed(list_float):
        delay = await value
        list_float_random_values.append(delay)

    return list_float_random_values
