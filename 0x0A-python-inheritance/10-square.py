#!/usr/bin/python3
"""The class Square will inherit from Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Init method."""

    def __init__(self, size):
        self.__size = size
        super().integer_validator("size", self.__size)

        Rectangle.__init__(self, self.__size, self.__size)
