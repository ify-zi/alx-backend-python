#!/usr/bin/env python3
""" annotated sum list """

from typing import Union, List


def sum_mixed_list(input_list: List[Union[int, float]]) -> float:
    """ return sum of floats in a list as float"""
    total: float = 0.00
    for i in input_list:
        total += i
    return float(total)
