#!/usr/bin/python3
"""Will inherit from Rectangle class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Because a square is a simillar to a rectangle,
    most methods and attributes will be inherited.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Will inherit attribute setter and getter from
        Rectangle class.
        size = width = height.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns a string representation of the instance."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)

    @property
    def size(self):
        """Getter for the attribute size."""
        return self.width

    @size.setter
    def size(self, value):
        "Sets the value of the attribute size"
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates the values of the attributes either by
        args or kwargs.
        """
        list_of_attributes = ['id', 'size', 'x', 'y']
        count = 0
        for arg in args:
            setattr(self, list_of_attributes[count], arg)
            count += 1

        if len(args) == 0:
            for attribute, value in kwargs.items():
                setattr(self, attribute, value)

    def to_dictionary(self):
        """Returns a dictionary representation of a Square object."""
        list_of_attributes = ['id', 'size', 'x', 'y']
        count = 0
        object_dict = {}

        for key in list_of_attributes:
            object_dict.update
            ({(key, getattr(self, list_of_attributes[count]))})
            count += 1

        return object_dict
