#!/usr/bin/python3


def best_score(a_dictionary):
    """Returns a key with the biggest integer value."""

    if a_dictionary is None:
        return None

    best_list = list(a_dictionary)
    best_key = best_list[0]

    for x in a_dictionary:
        if a_dictionary[x] > a_dictionary[best_key]:
            best_key = x

    return best_key
