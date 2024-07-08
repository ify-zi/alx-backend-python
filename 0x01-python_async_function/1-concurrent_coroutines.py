#!/usr/bin/env python3
"""
    MOdule of concurrent coroutines
"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ function definition """
    newList = []
    for _ in range(n):
        i = await wait_random(max_delay)
        newList.append(i)
    return sorted(newList)
