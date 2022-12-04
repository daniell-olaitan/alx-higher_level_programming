#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """Prints all the integers in a list, in reverse order

    Args:
        my_list: the given list
    """
    new_list = my_list[::-1]
    for integer in new_list:
        print("{:d}".format(integer))
