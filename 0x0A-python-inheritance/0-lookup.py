#!/usr/bin/python3
"""contains a function that lists all the attr of an object
"""


def lookup(obj):
    """returns the list of available attributes and method of an obj

    Args:
        obj: the given object
    """
    return dir(obj)
