#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    """A function that prints x elements of a list."""

    try:
        a = 0
        for n in my_list:
            print("{}".format(n), end='')
            a += 1
            if a == x:
                break

        print("")
        return a

    except IndexError:
        return a
