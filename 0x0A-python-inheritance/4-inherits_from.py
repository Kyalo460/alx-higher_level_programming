#!/usr/bin/python3
"""A function that uses isinstance to check if object inherited
directly or indirectly from an instance.
"""


def inherits_from(obj, a_class):
    """Returns True or False."""
    return bool(isinstance(obj, a_class))
