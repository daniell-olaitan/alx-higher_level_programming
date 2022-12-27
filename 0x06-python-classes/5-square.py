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
        self.size = size

    @property
    def size(self):
        """Gets the size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """computes the area of the square

        Returns:
            the computed area
        """
        return self.__size**2

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end='')

                print()
