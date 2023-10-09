#!/usr/bin/python3
"""Importing the class that I'm going to inherit."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This class will inherit from class BaseGeometry."""

    def __init__(self, width, height):
        """Calling function from BaseGeometry to validate values before storing them."""
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

