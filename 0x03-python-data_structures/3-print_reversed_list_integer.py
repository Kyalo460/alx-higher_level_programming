#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    """Prints a list in reverse order"""

    my_copy = my_list.copy()

    my_copy.reverse()

    for rev in my_copy:
        print("{:d}".format(rev))
