#!/usr/bin/python3
"""Function add_attribute
"""


def add_attribute(a_class, name, value):
    """Adds new attribute to an object if it's possible"""

    if hasattr(a_class, "__dict__"):
        setattr(a_class, name, value)

    raise TypeError("can't add new attribute")
