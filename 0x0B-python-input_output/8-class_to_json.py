#!/usr/bin/python3
"""contains a function that returns the dict description with simple
   data structure for json serialization
"""


def class_to_json(obj):
    """returns the dict description with simple data structure
       for json serialization
    """
    return vars(obj)
