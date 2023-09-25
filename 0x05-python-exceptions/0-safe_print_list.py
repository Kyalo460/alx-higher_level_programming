#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    """A function that prints x elements of a list."""

    num = 0

    try:
        for a in range(0, x):
            print("{}".format(my_list[a]), end='')
            num += 1

        print("")
        return num

    except IndexError:
        print("")
        return num
