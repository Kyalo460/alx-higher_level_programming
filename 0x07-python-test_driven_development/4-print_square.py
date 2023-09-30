#!/usr/bin/python3
"""This function draws a square using 
'#' with width of the integer argument given.
"""


def print_square(size):
    """If size is not an integer or is less than 0
    an exception will be raised.
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if size == 0:
        print()
        return

    for w in range(0, size):
        for l in range(0, size):
            print("#", end='')
        print()
