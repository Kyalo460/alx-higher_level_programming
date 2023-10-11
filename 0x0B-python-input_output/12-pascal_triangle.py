#!/usr/bin/python3
"""Makes a pastcal triangle using lists."""


def pascal_triangle(n):
    """If n is 0 then it returns an empty list.
    Otherwise it returns the representation of
    the triangle as list of list elements.
    """
    main_list = []
    if n == 0:
        return main_list

    sub_value = n - 1

    for row in range(0, n):
        sub_list = []

        for column in range(0, n - sub_value):
            if column == 0:
                sub_list.append(1)
                continue

            try:
                add_value = main_list[row - 1][column -
                                               1] + main_list[row - 1][column]

            except IndexError:
                add_value = 1

            sub_list.append(add_value)

        main_list.append(sub_list)
        sub_value -= 1

    return main_list
