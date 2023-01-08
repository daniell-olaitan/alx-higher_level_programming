#!/usr/bin/python3
"""module contains a locked class
"""


class LockedClass:
    """class prevents  that prevents the user from dynamically
       creating new instance attributes, except if the new instance
       attribute is called first_name.
    """

    __slots__ = ["first_name"]
