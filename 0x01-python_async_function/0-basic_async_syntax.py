#!/usr/bin/env python3
"""
    MOdle that uses the basic routine of async function
    to create a coroutine object
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ Fucntion defination of module """
    i = random.uniform(0, max_delay)
    await asyncio.sleep(i)
    return i
