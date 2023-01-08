#!/usr/bin/python3
"""A class that defines a rectangle"""


class Rectangle:
    """this represents a rectangle"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initializing this rectangle class
        Args:
            width: represents the width of the rectangle
            height: represents the height of the rectangle
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than zero
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """retrieves width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """retrieves height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets height attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """computes and returns the area of the rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """computes and returns the perimeter of the rectangle
        """
        if self.width != 0 and self.height != 0:
            return self.height*2 + self.width*2

        return 0

    def __str__(self):
        """returns the string rep of the rectangle"""
        res = []
        if self.perimeter() == 0:
            return ""

        for i in range(self.height):
            res.append(str(print_symbol) * self.width)

        return "\n".join(res)

    def __repr__(self):
        """returns the object rep of the rectangle"""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        print("Bye rectangle...")
        type(self).number_of_instnaces -= 1
