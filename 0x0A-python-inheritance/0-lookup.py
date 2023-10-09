#!/usr/bin/python3
"""This function will return the list of objects available in a class."""


def lookup(obj):
    """Will return list of available attributes and methods in object."""
    return dir(obj)