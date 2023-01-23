#!/usr/bin/python3
"""contains a class that defines the base class"""
import json
import os


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
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        filename = cls.__name__ + ".json"
        if list_objs is None:
            res = "[]"
        else:
            res = cls.to_json_string([o.to_dictionary() for o in list_objs])

        with open(filename, "w", encoding="utf-8") as fd:
            fd.write(res)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation 'json_string'"""
        if json_string is None or json_string == "":
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            obj = cls(1, 2)
        else:
            obj = cls(1)

        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = cls.__name__ + ".json"
        res = []
        if os.path.exists(filename):
            with open(filename, "r", encoding="utf-8") as fd:
                json_string = fd.read()
                list_of_dicts = cls.from_json_string(json_string)
                res = [cls.create(**attrs) for attrs in list_of_dicts]

                return res

        return res
