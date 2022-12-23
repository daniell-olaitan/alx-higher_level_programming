#!/usr/bin/python3
def safe_print_division(a, b):
    """Divides 2 integers and prints the result

    Args:
        a: the first int
        b: the second int

    Return:
        the result of the division
    """
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {:f}".format(result))
