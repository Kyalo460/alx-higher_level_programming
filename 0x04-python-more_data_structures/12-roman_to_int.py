#!/usr/bin/python3


def roman_to_int(roman_string):
    """Converts a Roman number to an integer"""

    if roman_string is None or isinstance(roman_string, str) is False:
        return 0

    a_dict = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    a_list = list(a_dict)
    add = 0
    prev = a_dict['M']

    for key in roman_string:
        for lett in a_list:
            if key == lett:
                break

        if prev < a_dict[key]:
            add -= prev * 2

        prev = a_dict[key]
        add += a_dict[key]

    return add
