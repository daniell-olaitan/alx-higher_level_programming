#!/usr/bin/python3
def element_at(my_list, idx):
    """Retrieves an element from a list like in C

    Args:
        my_list: the given list
        idx: given index

    Returns:
        None if idx is -ve or more than the length of my_list
    """
    list_length = len(my_list)
    if idx < 0 or idx >= list_length:
        return None

    return my_list[idx]
