#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """executes a function safely

    Args:
        fct: a pointer to the function to be executed
        args: the arguments to the function

    Returns:
        The result of the function or None if exception occurs
    """
    try:
        result = fct(*args)
    except Exception as exc:
        sys.stderr.write(f"Exception: {exc}\n")
        return None

    return result
