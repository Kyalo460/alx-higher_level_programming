#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Inside the class."""

    def __init__(self, size=0):
        """Private instance attribute.

        Args:
            size (int): The size of the new square.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an int")

        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
