#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    """Replaces an element and returns a copy"""

    limit = len(my_list) - 1
    new_list = my_list.copy()

    if idx > limit or idx < 0:
        return new_list

    new_list[idx] = element

    return new_list
