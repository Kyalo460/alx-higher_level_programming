#!/usr/bin/python3
"""A module that willl check if an object is an instance
of a class.
"""


def is_same_class(obj, a_class):
    """Will return True if an object is an instance and False
    if it is not.
    """

    return bool(isinstance(obj, a_class))
