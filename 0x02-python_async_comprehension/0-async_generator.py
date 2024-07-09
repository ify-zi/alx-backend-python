#!/usr/bin/env python3
"""
    async function comprehension modeule
"""

import asyncio
import random


async def async_generator():
    """function defination"""
    for count in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)
