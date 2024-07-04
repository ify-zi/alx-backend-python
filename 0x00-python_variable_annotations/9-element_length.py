#!/usr/bin/env python3
""" Using Iterable sequence in typing"""

from typing import List, Sequence, Iterable, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Using Iterables """
    return [(i, len(i)) for i in lst]
