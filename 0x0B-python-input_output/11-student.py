#!/usr/bin/python3

"""A class Student that contains
a students details.
"""


class Student:

    """Will contain attribut s that defines
    the student and a method to retrieve
    the student's details.
    """

    def __init__(self, first_name, last_name, age):
        """assigns values to attributs when
        class is instatiated.
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attr=None):
        """Returns a dictionary that has
         attribute:value.
        """

        if attr is None:
            return vars(self)

        attr_dict = {}
        for attribute in attr:
            try:
                getattr(self,  attribute)
            except AttributeError:
                continue

            attr_dict.update({attribute: getattr(self, attribute)})

        return attr_dict

    def reload_from_json(self, json):
        """Replaces attribute values with the new
        values stored in 'json' dict.
        """

        for attribute in json:
            setattr(self, attribute, json[attribute])
