#!/usr/bin/python3
"""Contains a class that defines a rectangle class 'Rectangle'
"""


class Rectangle:
    """defines a rectangle
    """
    def __init__(self, width=0, height=0):
        """initialises __width and __height

        Args:
            width: ..
            height: ..

        raises:
            TypeError: when int is not given
            ValueError: when value is < 0
        """
        self.width = width
        self.height = height

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
