#!/usr/bin/python3
"""A class Rectangle that defines a rectangle."""


class Rectangle:
    """This is where I define the attributes."""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

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
                string += "#"

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


Rectangle = __import__('4-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print(str(my_rectangle))
print("--")
print(my_rectangle)
print("--")
print(repr(my_rectangle))
print("--")
print(hex(id(my_rectangle)))
print("--")

# create new instance based on representation
new_rectangle = eval(repr(my_rectangle))
print(str(new_rectangle))
print("--")
print(new_rectangle)
print("--")
print(repr(new_rectangle))
print("--")
print(hex(id(new_rectangle)))
print("--")

print(new_rectangle is my_rectangle)
print(type(new_rectangle) is type(my_rectangle))
