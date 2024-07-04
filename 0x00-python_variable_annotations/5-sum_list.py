#!/usr/bin/env python3
""" annotated sum list """

from typing import List


def sum_list(input_list: List[float]) -> float:
    """ return sum of floats in a list as float"""
    total: float = 0.00
    for i in input_list:
        total += i
    return float(total)
