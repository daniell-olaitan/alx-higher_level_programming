#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """Deletes the item at a specific position in a list

    Args:
        my_list: the given list
        idx: the given index

    Returns:
        the new list
    """
    if idx < 0 or idx >= len(my_list):
        return my_list

    del my_list[idx]
