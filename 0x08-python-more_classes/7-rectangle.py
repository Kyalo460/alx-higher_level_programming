#!/usr/bin/python3
"""A class Rectangle that defines a rectangle."""


class Rectangle:
    """This is where I define the attributes."""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """Returns the area of a rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Returns the perimeter of a rectangle."""
        if self.width == 0 or self.height == 0:
            return 0

        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """Returns a string that is a repsentation of
        the rectangle by using #.
        """
        if self.width == 0 or self.height == 0:
            return ''

        string = ''

        for h in range(0, self.height):
            for w in range(0, self.width):
                string += str(self.print_symbol)

            if h == self.height - 1:
                break
            string += "\n"

        return string

    def __repr__(self):
        """Returns the information of the way the instance
        was created.

        ie. the class called and the arguments given.
        """

        return "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"

    def __del__(self):
        """Prints a message after object is deleted."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
