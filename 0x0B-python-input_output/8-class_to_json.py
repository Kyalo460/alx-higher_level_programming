#!/usr/bin/python3
"""Will return a serializable dict for JSON"""


def class_to_json(obj):
    """Will return a dictionary that represents the class's
    attributes and values.
    """

    return vars(obj)
