#!/usr/bin/env python3
""" Using Union and List for annotated """

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ returns a tuple of the annoated variables"""
    return (k, (v**2))
