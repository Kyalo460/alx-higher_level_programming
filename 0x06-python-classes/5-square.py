#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Inside the class."""

    def __init__(self, size=0):
        """Public instance attribute."""
        self.size = size

    def area(self):
        """Returns the square."""
        return self.__size ** 2

    @property
    def size(self):
        """A getter used to retrieve the length of a square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the length of a square."""
        if not isinstance(value, int):
            raise TypeError("size must be an int")

        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def my_print(self):
        """Prints the Square with #."""
        if self.__size == 0:
            print("")
            return

        for i in range(0, self.__size):
            for j in range(0, self.__size):
                print("#", end='')
            print("")
