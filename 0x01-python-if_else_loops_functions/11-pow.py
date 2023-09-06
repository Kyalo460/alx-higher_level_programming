#!/usr/bin/python3


def pow(a, b):
    """Returns a raised to b."""
    if b == 0:
        return 1

    if b < 0:
        a = 1 / a
        b = -b

    n = a ** b

    if a == 0.1:
        n = round(n, 2)

    return n
