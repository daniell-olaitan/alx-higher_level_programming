#!/usr/bin/python3
"""contains a class that defines Rectange"""
from models.base import Base


class Rectangle(Base):
    """defines a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """gets and sets the attr"""
        return self.__width

    @width.setter
    def width(self, value):
        self.validate_variable("width", value)
        self.__width = value

    @property
    def height(self):
        """gets and sets the attr"""
        return self.__height

    @height.setter
    def height(self, value):
        self.validate_variable("height", value)
        self.__height = value

    @property
    def x(self):
        """gets and sets the attr"""
        return self.__x

    @x.setter
    def x(self, value):
        self.validate_variable("x", value, False)
        self.__x = value

    @property
    def y(self):
        """gets and sets the attr"""
        return self.__y

    @y.setter
    def y(self, value):
        self.validate_variable("y", value, False)
        self.__y = value

    def area(self):
        """computes and returns the area of the rectangle"""
        return self.width * self.height

    def display(self):
        """displays the rectangle using '#'"""
        rect = ['#' * self.width] * self.height
        print('\n'.join(rect))

    def __str__(self):
        sp = "[Rectangle]"
        s = f"{sp} ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"
