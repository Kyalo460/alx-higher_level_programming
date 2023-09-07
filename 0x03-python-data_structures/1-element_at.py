#!/usr/bin/python3


def element_at(my_list, idx):
    """Returns element at idx(index) from a list"""

    limit = len(my_list) - 1

    if idx > limit or idx < 0:
        return None

    a = my_list[idx]

    return a
