#!/usr/bin/python3
"""Contains a class that defines a square
"""


class Square:
    """Defines a square

    Attributes:
        __size: the length of the square
    """
    def __init__(self, size=0, position=(0,0)):
        """initializes size

        Args:
            size: the size of the square
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """gets and sets the position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        if (type(value) is tuple and
            len(value) == 2 and
            type(value[0]) is int and
            type(value[1]) is int and
            value[0] >= 0 and
            value[1] >= 0):
            #end of if
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """computes the area of the square

        Returns:
            the computed area
        """
        return self.size**2

    def my_print(self):
        """prints the square using '#'
        """
        if self.size == 0:
            print()
        else:
            for i in range(self.size):
                for j in range(self.position[0]):
                    print(" ", end="")
                for j in range(self.size):
                    print("#", end='')

                print()
