#!/usr/bin/python3
"""contains magic calculation function
"""


def magic_calculation(a, b):
    """magic calc func

    Args:
        a: ...
        b: ...

    Return:
        result
    """
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')

            result += a**b / i
        except:
            result = b + a
            break

    return result
