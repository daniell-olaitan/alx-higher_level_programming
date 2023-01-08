#!/usr/bin/python3
"""Contains a function that prints string of first and last names
"""


def say_my_name(first_name, last_name=""):
    """prints 'My name is <first_name> <last_name>

    Args:
        first_name: first name
        last_name: last name
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    elif type(last_name) is not str:
        raise TypeError("last_name must be a string")
    else:
        print(f"My name is {first_name} {last_name}")
