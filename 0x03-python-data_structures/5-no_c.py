#!/usr/bin/python3
def no_c(my_string):
    """Removes all characters c and C from a string

    Args:
        my_string: the given string

    Returns:
        the new string
    """
    str_list = [ch for ch in my_string if ch != 'c' and ch != 'C']
    return ''.join(str_list)

print(no_c('Best School Chicago'))
