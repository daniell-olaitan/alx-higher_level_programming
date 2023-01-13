#!/usr/bin/python3
"""implements square class from rectangle class"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """defines square"""

    def __init__(self, size):
        """initializes size and validates it size"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
