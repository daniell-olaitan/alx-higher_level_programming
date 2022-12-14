#!/usr/bin/python3
def safe_print_integer(value):
    """Prints an integer with '"{:d}".formart()'

    Args:
        value: the int to be printed

    Return:
        True: if the value has be correctly printed
        False: if otherwise
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
