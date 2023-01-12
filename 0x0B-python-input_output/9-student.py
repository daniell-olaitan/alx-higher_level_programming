#!/usr/bin/python3
"""contains a class that defines a student"""


class Student:
    """a class that defines a student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dict representation of a Student instance"""
        return vars(self)
