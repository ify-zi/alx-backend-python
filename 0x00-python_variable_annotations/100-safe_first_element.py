#!/usr/bin/env python3
""" Returns the first element of a list """

from typing import Union, Any, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ return first function in a list """
    if lst:
        return lst[0]
    else:
        return None
