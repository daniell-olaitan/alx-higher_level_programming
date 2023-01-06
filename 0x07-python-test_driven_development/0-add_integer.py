#!/usr/bin/python3
"""Contains a function that adds two integers.
"""


def add_integer(a, b=98):
    """Adds two integers

    Args:
        a: the first integer
        b: second int (default value of 98)

    Return:
        the result of the addition
    """
    types = [int, float]
    if (type(a) not in types) or (type(b) not in types):
        if type(a) not in types:
            raise TypeError("a must be an integer")
        else:
            raise TypeError("b must be an integer")

    else:
        return int(a) + int(b)
