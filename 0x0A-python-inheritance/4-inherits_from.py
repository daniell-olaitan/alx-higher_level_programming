#!/usr/bin/python3
"""contains a func that determines if an objs class inherits from a class"""


def inherits_from(obj, a_cass):
    """determines if an objs class inherites from a class"""
    return issubclass(type(obj), a_class)
