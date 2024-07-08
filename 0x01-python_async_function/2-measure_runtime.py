#!/usr/bin/env python3
""" Module that measure the runtime of each
    Async calls
"""

import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ function definiation of module"""
    r_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    time_elasped = time.perf_counter() - r_time
    return time_elasped/n
