#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    """Prints elements in a matrix"""
    if len(matrix[0]) == 0:
        print('')
        return 1

    for x in range(0, len(matrix)):
        for y in matrix[x]:
            print("{:d}".format(y), end='')

            if y == matrix[x][len(matrix[x]) - 1]:
                continue
            print(' ', end='')

        print('')
