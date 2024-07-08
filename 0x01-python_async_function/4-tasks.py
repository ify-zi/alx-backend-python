#!/usr/bin/env python3
"""
    MOdule of concurrent coroutines
"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ function definition """
    newList = []
    for _ in range(n):
        i = await task_wait_random(max_delay)
        newList.append(i)
    return sorted(newList)
