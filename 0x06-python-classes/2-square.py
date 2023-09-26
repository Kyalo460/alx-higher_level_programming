#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Inside the class."""

    def __init__(self, size=0):
        """Private instance attribute."""
        self.__size = size

        if type(size) is not int:
            raise TypeError("size must be an int")

        if size < 0:
            raise ValueError("size must be >= 0")
