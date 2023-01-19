#!/usr/bin/python3
"""contains a class that defines the base class"""
import json


class Base:
    """defines the base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @staticmethod
    def validate_variable(name, value, greater=True):
        """validates an assigned variable"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            if greater:
                raise ValueError(f"{name} must be > 0")
            elif value < 0:
                raise ValueError(f"{name} must be >= 0")

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return '[]'

        return json.dumps(list_dictionaries)
