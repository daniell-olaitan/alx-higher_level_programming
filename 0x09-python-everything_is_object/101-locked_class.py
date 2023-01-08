#!/usr/bin/python3
"""module contains a locked class
"""


class LockedClass:
    """class prevents  that prevents the user from dynamically
       creating new instance attributes, except if the new instance
       attribute is called first_name.
    """

    def __setattr__(self, name, value):
        if name == "first_name":
            self.__dict__[name] = value
        else:
            err = f"'LockedClass' object has not \attribute '{name}'"
            raise AttributeError(err)
