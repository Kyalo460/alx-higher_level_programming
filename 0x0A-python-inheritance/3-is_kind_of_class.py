#!/usr/bin/python3
"""A module that will check if an object is an instance of a class
or parent class.
"""


def is_kind_of_class(obj, a_class):
    """Will use isinstance to return True or False."""
    return bool(isinstance(obj, a_class))
