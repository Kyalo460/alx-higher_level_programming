#!/usr/bin/python3


def pow(a, b):
    """Returns a raised to b."""
    if b == 0:
        return 1

    if b < 0:
        a = 1 / a
        b = -b

    prod = a
    for n in range(1, b):
        n = prod * a
        prod = n

    return n
