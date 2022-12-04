#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """Replaces an element in a list

    Args:
        my_list: the given list
        idx: the index of the element to replace
        element: the element to insert in the list

    Returns:
         The new list
    """
    if idx < 0 or idx >= len(my_list):
        return my_list

    my_list[idx] = element
    return my_list
