#!/usr/bin/python3


def only_diff_elements(set_1, set_2):
    """Returns a set of all elements present in only one set."""

    od_set = {x for x in set_1 if x not in set_2}
    od_set.update({x for x in set_2 if x not in set_1})

    return od_set
