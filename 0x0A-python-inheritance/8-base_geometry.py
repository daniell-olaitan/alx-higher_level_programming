#!/usr/bin/python3
"""defines geometry"""
BaseGeometry = __import__("7-base_geometry.py").BaseGeometry


class Rectangle(BaseGeometry):
    """defines rectangle geometry"""

    def __init__(self, width, height):
        """instantiates and validates width and height of the rectangle"""
        self.integer_validator("width", width)
        self.integer_vaidator("height", height)
        self.__width = width
        self.__height = height
