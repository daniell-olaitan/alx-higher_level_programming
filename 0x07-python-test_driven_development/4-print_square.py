#!/usr/bin/python3
"""contains a function that prints a square using '#'
"""


def print_square(size):
    """prints a square of size 'size' using '#'

    Args:
        size: the size of the square
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if size == 0:
        print()
    else:
        for i in range(size):
            print('#' * size)
