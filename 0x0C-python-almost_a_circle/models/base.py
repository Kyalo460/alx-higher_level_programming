#!/usr/bin/python3
"""This will be the base of all the other classes."""
import json
import models


class Base:
    """The purpose of this class is to manage the id attribute
    in all future classes.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes the id attribute and increments
        the __nb_objects class attribute each time an instance
        is created.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns json string that has a list of dictionaries."""
        if list_dictionaries is None:
            return json.dumps([])

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Saves list_objs to a file as a json string."""
        new_list = []
        for obj in list_objs:
            if type(obj) is models.rectangle.Rectangle:
                list_of_attributes = ['id', 'width', 'height', 'x', 'y']
            elif type(obj) is models.square.Square:
                list_of_attributes = ['id', 'size', 'x', 'y']
            else:
                raise TypeError("The object does not exist")

            object_dict = {}
            for name in list_of_attributes:
                object_dict.update({(name, getattr(obj, name))})

            new_list.append(object_dict)

        json_string = cls.to_json_string(new_list)
        filename = cls.__name__ + '.json'

        with open(filename, 'w', encoding='utf-8') as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """Deserializes a json_string and returns the list."""
        if json_string is None or len(json_string) == 0:
            return []

        decoded_list = json.loads(json_string)
        return decoded_list

    @classmethod
    def create(cls, **dictionary):
        """Returns an object with set attributes."""
        if cls.__name__ == "Rectangle":
            dummy_instance = models.rectangle.Rectangle(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = models.square.Square(1)
        else:
            raise NameError("That class does not exist")

        dummy_instance.update(**dictionary)

        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """Returns a list of new instances."""
        filename = cls.__name__ + '.json'

        json_string = ''
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                for line in file:
                    json_string += line

        except FileNotFoundError:
            return []

        deserialized_list = cls.from_json_string(json_string)

        new_object_list = []
        for obj in deserialized_list:
            if cls.__name__ == "Rectangle":
                new_object = models.rectangle.Rectangle.create(**obj)
            elif cls.__name__ == "Square":
                new_object = models.square.Square.create(**obj)
            else:
                raise NameError("That class does not exist")
            new_object_list.append(new_object)

        return new_object_list
