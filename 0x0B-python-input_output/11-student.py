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
        var = vars(self)
        if attrs:
            res = {}
            for key in attrs:
                if key in var:
                    res[key] = var[key]

            return res

        return vars(self)

    def reload_from_json(self, json):
        """replaces all the attr of the Student obj"""
        var = vars(self)
        for attr, value in json.items():
            if attr in var:
                setattr(self, attr, value)
