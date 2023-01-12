#!/usr/bin/python3
"""contains that returns a pascal triangle of a given length"""


def pascal_triangle(n):
    """returns a pascal triangle of a given length"""
    res []
    if n <= 0:
        return res

    for i in range(n):
        tmp = []
        for j in range(i+1):
            if (j == 0) or (j == i):
                tmp.append(1)
            else:
                tmp.append(res[-1][j] + res[-1][j-1])

        res.append(tmp)
