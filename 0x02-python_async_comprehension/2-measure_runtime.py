#!/usr/bin/env python3
"""
    measure time performance of async function
"""

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """function definition"""
    t_time = time.perf_counter()
    await asyncio.gather(async_comprehension(),
                         async_comprehension(),
                         async_comprehension(),
                         async_comprehension()
                         )
    r_time = time.perf_counter() - t_time
    return r_time
