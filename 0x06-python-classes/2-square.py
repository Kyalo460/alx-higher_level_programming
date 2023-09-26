#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Inside the class."""

    def __init__(self, size=0):
        """Private instance attribute."""
        self.__size = size

        if type(size) is not int:
            print("size must be an int", end='')
            raise TypeError

        if size < 0:
            print("size must be >= 0", end='')
            raise ValueError
