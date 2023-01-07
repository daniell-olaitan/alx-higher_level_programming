#!/usr/bin/python3
"""contains a class that defines a rectangle"""


class Rectangle:
    """defines a rectangle
    """
    @property
    def width(self):
        """getter retrieves __width
           setter sets __width to int and >= 0
        """
        return self.__width

    @width.setter
    def width(self, value):
        if type(width) not int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """getter retrieves __height
           setter sets __height to int and >= 0
        """
        return self.__height

    @height.setter
    def height(self, value):
        if type(height) not int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def __init__(self, width=0, height=0):
        """initialises __width and __height
        """
        self.width = width
        self.height = height

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
        res = []
        if self.perimeter == 0:
            return ""

        for i in range(self.height):
            res.append("#" * self.width)

        return "\n".join(res)
