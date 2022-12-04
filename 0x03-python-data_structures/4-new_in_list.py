#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Replaces an element in a list without doing it in place

    Args:
        my_list: the given list
        idx: the index of the element to replace
        element: the element to insert into the list

    Returns:
        the new list
    """
    new_list = my_list[:]
    if idx < 0 or idx >= len(my_list):
        return new_list

    new_list[idx] = element
    return new_list
