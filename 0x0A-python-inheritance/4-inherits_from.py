#!/usr/bin/python3
"""contains a func that determines if an obj's class inherits from a class"""


def inherites_from(obj, a_cass):
    """determines if an obj's class inherites from a class"""
    return issubclass(type(obj), a_class)
