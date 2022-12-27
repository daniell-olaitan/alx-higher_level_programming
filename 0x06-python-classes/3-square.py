#!/usr/bin/python3
"""Contains a class that defines a square
"""


class Square:
    """Defines a square

    Attributes:
        __size: the length of the square
    """
    def __init__(self, size=0):
        """initializes size

        Args:
            size: the size of the square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """computes the area of the square

        Returns:
            the computed area
        """
        return size**2
