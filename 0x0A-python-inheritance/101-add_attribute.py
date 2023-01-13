#!/usr/bin/python3
"""this module defines a function that adds attributes to objects"""


def add_attribute(a_class, name, value):
    """Add a new attribute to an object if possible
    """
    if not hasattr(a_class, "__dict__"):
        raise TypeError("can't add new attribute")

    setattr(a_class, name, value)
