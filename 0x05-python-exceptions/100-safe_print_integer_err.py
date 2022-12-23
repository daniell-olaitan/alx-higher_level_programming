#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    """Prints an integer

    Args:
        value: the int to be printed

    Return:
        True: if the value has be correctly printed
        False: if otherwise
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError) as exc:
        sys.stderr.write(f"Exception: {exc}\n")
        return False
