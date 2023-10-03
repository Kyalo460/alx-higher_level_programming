#!/usr/bin/python3
"""A function that divides all elements in a matrix
by an integer or float.
"""


def matrix_divided(matrix, div):
    """Returns: a new matrix of the result of the division.

    The numbers in the new matrix are rounded up to the nearest
    second decimal place if there is more than 1 decimal place.
    """

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    last = len(matrix)
    size = len(matrix[0])

    for i in range(0, last):
        if size != len(matrix[i]):
            raise TypeError("Each row of the matrix must have the same size")

    for n in matrix:
        for j in n:
            if type(j) not in [int, float]:
                raise TypeError("matrix must be a matrix \
                        (list of lists) of integers/floats")

    new_matrix = []
    new_list = []
    for i in range(0, last):
        for j in matrix[i]:
            new_list.append(round(j / div, 2))
        new_matrix.append(new_list)
        new_list = []

    return new_matrix
