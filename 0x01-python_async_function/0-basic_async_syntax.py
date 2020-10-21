#!/usr/bin/env python3
import random
import asyncio
"""
==============================================================================
asynchronous coroutine that takes in an integer argument (max_delay, with
a default value of 10) named wait_random that waits for a random delay between
 0 and max_delay (included and float value) seconds and eventually returns it.
==============================================================================
"""


async def wait_random(max_delay=10):
    """
    :param max_delay:
    :return: a float random value
    """
    random_value = random.uniform(0, max_delay)
    await asyncio.sleep(random_value)
    return random_value