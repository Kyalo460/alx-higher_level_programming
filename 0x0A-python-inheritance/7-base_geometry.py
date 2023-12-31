#!/usr/bin/python3
"""Making a class called BaseGeometry."""


class BaseGeometry:
    """Defining methods and attributes."""

    def area(self):
        """Raises an exception + an error message."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the value if it is an integer and is greater than 0."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value < 1:
            raise ValueError("{} must be greater than 0".format(name))
