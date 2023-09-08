#!/usr/bin/python3


def no_c(my_string):
    """Removes characters from a string."""

    new_string = ""
    _list = []

    for n in my_string:
        if n == 'c' or n == 'C':
            continue
        _list.append(n)

    for m in _list:
        new_string += m

    return new_string
