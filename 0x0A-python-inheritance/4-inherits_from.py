#!/usr/bin/python3
"""A function that uses isinstance to check if object inherited
directly or indirectly from an instance.
"""


def inherits_from(obj, a_class):
    """Returns True or False."""
    if type(obj) is a_class:
        return False

    return bool(issubclass(obj.__class__, a_class))
