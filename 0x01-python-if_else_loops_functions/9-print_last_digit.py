#!/usr/bin/python3


def print_last_digit(number):
    """prints and returns last digit"""
    if number < 0:
        number = -number % 10
    else:
        number = number % 10

    print("{}".format(number), end='')

    return number
