#!/usr/bin/env python3
""" Typing module using callable"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ returns function using callable"""
    return (lambda x: x * multiplier)
