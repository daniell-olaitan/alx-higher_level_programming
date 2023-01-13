#!/usr/bin/python3
"""contains a func that determines if an objs class inherits from a class"""


def inherits_from(obj, a_cass):
    """determines if an objs class inherites from a class"""
    cls = type(obj)
    if cls is a_class:
        return False

    return issubclass(cls, a_class)
