#!/usr/bin/python3


def uniq_add(my_list=[]):
    """Adds uniques elements in a list."""

    add = 0

    for n in set(my_list):
        add += n

    return add
