#!/usr/bin/python3
"""contains a class that defines a student"""


class Student:
    """a class that defines a student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dict representation of a Student instance"""
        if type(attrs) is list and all(type(e) == str for e in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}

        return vars(self)

    def reload_from_json(self, json):
        """replaces all the attr of the Student obj"""
        for attr, value in json.items():
            if hasattr(self, attr):
                setattr(self, attr, value)
