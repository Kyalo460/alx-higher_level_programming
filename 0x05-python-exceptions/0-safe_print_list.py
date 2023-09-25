#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    """A function that prints x elements of a list."""

    a = 0

    try:
        for a in range(0, x):
            print("{}".format(my_list[a]), end='')

        print("")
        return a + 1

    except IndexError:
        print("")
        return a
