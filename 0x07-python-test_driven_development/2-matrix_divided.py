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
    if div == 0:
        raise ZeroDivisionError('division by zero')

    if (type(matrix) is not list or
        sum(1 for _ in filter(lambda x: type(x) is not list, matrix)) != 0 or
        sum(1 for _ in filter(lambda x: type(x) not in [int, float],
                              [c for e in matrix for c in e])) != 0):
        raise TypeError(list_err)

    elif len({len(e) for e in matrix}) > 1:
        raise TypeError(size_err)

    elif type(div) not in [int, float]:
        raise TypeError('div must be a number')

    else:
        for e in matrix:
            res.append([round(i/div, 2) for i in e])

        return res
