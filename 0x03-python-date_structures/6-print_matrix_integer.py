#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """Prints a matrix of integers

    Args:
        matrix: the given matrix of numbers
    """
    for row in matrix:
        row_len = len(row) - 1
        i = 0
        for element in row:
            if i == row_len:
                print("{}".format(element))
            else:
                print("{} ".format(element), end='')

            i += 1
