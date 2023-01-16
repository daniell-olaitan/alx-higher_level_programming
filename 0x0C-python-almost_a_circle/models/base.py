#!/usr/bin/python3
"""contains a class that defines the base class"""


class Base:
    """defines the base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            super().__nb_objects += 1
            self.id = super().__nb_objects
