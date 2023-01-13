#!/usr/bin/python3
"""contains a function that determines if an obj is an inst of a class"""


def is_same_class(obj, a_class):
    """determines if the object obj is an instance of class a_class"""
    return type(obj) is a_class
