#!/usr/bin/python3
"""This class will inherit from Base."""
from models.base import Base


class Rectangle(Base):
    """Defines a rectangele by having attributes that store
    width, height, x, and y.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes the attributes given as arguments."""

        self.width = width
        self.height = height
        self.x = x
        self.y = y

        super().__init__(id)

    @property
    def width(self):
        """Gets the width value."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width value."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Gets the height value."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height value."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Gets the x value."""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the x value."""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Gets the y value."""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the y value."""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area of the rectangle."""
        return self.height * self.width

    def display(self):
        """Prints the instance with #."""
        for skip in range(0, self.y):
            print()
        for height in range(0, self.height):
            for space in range(0, self.x):
                print(" ", end='')
            for width in range(0, self.width):
                print("#", end='')
            print()

    def __str__(self):
        """Returns a string that displays the values of the
        instance.
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Updates attributes provided chronoligically.
        The order is: id, width, height, x, y.
        """
        list_of_attributes = ['id', 'width', 'height', 'x', 'y']
        count = 0
        for arg in args:
            setattr(self, list_of_attributes[count], arg)
            count += 1

        if len(args) == 0:
            for atrribute, value in kwargs.items():
                setattr(self, atrribute, value)

    def to_dictionary(self):
        """Returns a dictionary representantion of an object."""
        list_of_attributes = ['id', 'width', 'height', 'x', 'y']
        count = 0
        object_dict = {}

        for key in list_of_attributes:
            object_dict.update(
                {(key, getattr(self, list_of_attributes[count]))})
            count += 1

        return object_dict
