#!/usr/bin/python3
"""Contains function that divides a matrix
"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix

    Args:
        matrix: list of lists of integers or floats
        div: divisor (must be int or float)

    Return:
        a new matrix containing the qotients of the divisions
    """
    list_err = "matrix must be a matrix (list of lists) of integers/floats"
    size_err = "Each row of the matrix must have the same size"
    res = []
    if (type(matrix) is not list or
        len(matrix) < 2 or
        sum(1 for _ in filter(lambda x: type(x) is not list, matrix)) != 0 or
        sum(1 for _ in filter(lambda x: len(x) < 2, matrix)) != 0 or
        sum(1 for _ in filter(lambda x: type(x) not in [int, float],
                              [e[i] for e in matrix for i, j in matrix]) != 0):
        raise TypeError(list_err)
    else:
        
