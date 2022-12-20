#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """Prints a matrix of integers

    Args:
        matrix: the given matrix of numbers
    """
    if matrix[0]:
        for row in matrix:
            row_len = len(row)
            i = 1

            for element in row:
                if i == row_len:
                    print("{:d}".format(element))
                else:
                    print("{:d} ".format(element), end='')

                    i += 1
