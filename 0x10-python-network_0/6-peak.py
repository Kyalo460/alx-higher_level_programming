#!/usr/bin/python3
"""A method that finds the peak in list of integers"""


def find_peak(list_of_integers):
    """list_of_integers should not be empty"""
    size = len(list_of_integers)
    if size == 0:
        return
    if size == 1:
        return list_of_integers[0]
    if size == 2:
        return max(list_of_integers)

    mid = int(size / 2)
    peak = list_of_integers[mid]
    if peak > list_of_integers[mid - 1] and peak > list_of_integers[mid + 1]:
        return peak
    elif peak <= list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid + 1:])
