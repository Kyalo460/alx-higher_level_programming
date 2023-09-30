#!/usr/bin/python3
"""A function that will add integers."""


def add_integer(a, b=98):
    """b is set to default 98.
    both a and b if inputed should be integers or floats
    if not an exception will be raised.

    Returns: the sum of a and b
    """

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")

    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    if type(a) is float:
        a = int(a)

    if type(b) is float:
        b = int(b)

    return a + b
