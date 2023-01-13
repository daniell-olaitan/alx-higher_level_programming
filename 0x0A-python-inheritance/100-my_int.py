#!/usr/bin/python3
"""contains a class that defines a rebel integer"""


class MyInt(int):
    """defines a rebel integer"""

    def __eq__(self, obj):
        """not equal"""
        return super().real != obj

    def __ne__(self, obj):
        """equal"""
        return super().real == obj

my_i = MyInt(3)
print(my_i)
print(my_i == 3)
print(my_i != 3)
