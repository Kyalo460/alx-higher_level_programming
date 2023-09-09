#!/usr/bin/python3


def search_replace(my_list, search, replace):
    """Replaces all occurrences of an element by another in a new list."""

    new_list = []

    for n in my_list:
        if n == search:
            n = replace
        new_list.append(n)

    return new_list
