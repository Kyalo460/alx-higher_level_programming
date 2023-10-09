#!/usr/bin/python3
"""Importing the class that I'm going to inherit."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This class will inherit from class BaseGeometry."""

    def __init__(self, width, height):
        """Calling function from BaseGeometry to validate values
        before storing them.
        """
        self.__width = width
        self.__height = height
        super().integer_validator("width", self.__width)
        super().integer_validator("height", self.__height)

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """Will have an implementation of area."""
        return self.__width * self.__height
