#!/usr/bin/python3
"""A class Student that contains
a students details.
"""


class Student:
    """Will contain attributes that defines
    the student and a method to retrieve
    the student's details.
    """

    def __init__(self, first_name, last_name, age):
        """assigns values to attributes when
        class is instatiated.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns a dictionary that has 
        attribute:value.
        """
        return vars(self)
