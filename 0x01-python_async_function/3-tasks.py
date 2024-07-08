#!/usr/bin/env python3
""" Module of creating a asyncio.task object"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """ fucntion definition """
    return asyncio.create_task(wait_random(max_delay))
