#!/usr/bin/python3
"""A class that will ingherit from the class list."""


class MyList(list):
    """Will have a method that prints a sorted list of integers."""

    def __init__(self):
        """Initializes attributes of the class."""
        super(list).__init__(list)

    def print_sorted(self):
        """Prints a sorted list of integers."""
        sorted_list = sorted(self)
        print("{}".format(sorted_list))
