#!/usr/bin/python3


def replace_in_list(my_list, idx, element):
    """Replaces an element at idx (index)."""

    limit = len(my_list) - 1

    if idx > limit or idx < 0:
        return my_list

    my_list[idx] = element

    return my_list
