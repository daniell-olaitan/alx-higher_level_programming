#!/usr/bin/python3
def max_integer(my_list=[]):
    """Finds the biggest integer in a list with using max()

    Args:
        my_list: the given list of integers

    Returns:
        the biggest integer in the list my_list
    """
    list_len = len(my_list)
    if list_len == 0:
        return None

    max_value = my_list[0]
    for value in my_list:
        if value > max_value:
            max_value = value

    return max_value
