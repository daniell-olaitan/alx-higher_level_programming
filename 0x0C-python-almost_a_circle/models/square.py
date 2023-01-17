#!/usr/bin/python3
"""contains class that defines square shape"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """defines square shape"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """updates the attributes of the square object"""
        arg_len = len(args)
        if arg_len >= 2:
            args = list(args)
            args.insert(1, args[1])

        if (arg_len == 0) and ("size" in kwargs):
            self.size = kwargs["size"]

        super().update(*args, **kwargs)

    def to_dictionary(self):
        """returns the dictionary representation of the obj"""
        res = {}
        for key in ["id", "size", "x", "y"]:
            res[key] = getattr(self, key)

        return res
