#!/usr/bin/python3
"""MyInt inherits from int
"""


class MyInt(int):
    """Inherits from int
    """

    def __eq__(self, value):
        """Magic method equals
        """

        return super().__ne__(value)

    def __ne__(self, value):
        """Magic method not equals
        """

        return super().__eq__(value)
