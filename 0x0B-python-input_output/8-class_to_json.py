#!/usr/bin/python3
"""contains a function that returns the dict description with simple
   data structure for json serialization
"""
import json


def class_to_json(obj):
    """returns the dict description with simple data structure
       for json serialization
    """
    return vars(obj)
