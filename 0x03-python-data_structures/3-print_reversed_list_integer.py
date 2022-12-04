#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """Prints all the integers in a list, in reverse order

    Args:
        my_list: the given list
    """
    if my_list:
        for integer in my_list[::-1]:
            print("{:d}".format(integer))
