#!/usr/bin/env python3
"""
===============================================================================
From the previous file, import wait_n into 2-measure_runtime.py.
Create a measure_time function with integers n and max_delay as arguments that
measures the total execution time for wait_n(n, max_delay), and returns
 total_time / n. Your function should return a float.
Use the time module to measure an approximate elapsed time.
===============================================================================
"""
import time
import asyncio


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int = 0, max_delay: int = 10) -> float:
    """
        :param n: times to calculate random values
        :param max_delay: maximum time delay
        :return: a float value with the execution time
    """
    starting_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    finishing_time = time.perf_counter()
    prom_time = (finishing_time - starting_time) / n

    return prom_time
