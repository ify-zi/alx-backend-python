#!/usr/bin/env python3
"""
    async function comprehension modeule
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """function defination"""
    for count in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)
