#!/usr/bin/python3
"""A function that prints out a sentence that
says what your name is.
"""


def say_my_name(first_name, last_name=""):
    """If first or last name is not a string
    an error will be raised."""

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")

    if last_name is not "":
        if type(last_name) is not str:
            raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))
