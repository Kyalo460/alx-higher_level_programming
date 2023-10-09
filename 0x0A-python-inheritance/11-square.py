#!/usr/bin/python3
"""The class Square will inherit from Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Init method."""

    def __init__(self, size):
        self.__size = size
        super().integer_validator("size", self.__size)

    def area(self):
        """Returns the area of a square."""
        return self.__size * self.__size

    def __str__(self):
        """Returns a string to print."""
        return "[Square] {}/{}".format(self.__size, self.__size)
