#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    """Prints the first x elements of a list and only integers."""

    num = 0

    try:
        for a in range(0, x):

            if type(my_list[a]) is int:
                print("{:d}".format(my_list[a]), end='')
                num += 1

            else:
                continue

        print("")
        return num

    except ValueError:
        return num
