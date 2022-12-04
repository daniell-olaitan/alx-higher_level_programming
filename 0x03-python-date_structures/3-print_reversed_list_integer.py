#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """Prints all the integers in a list, in reverse order

    Args:
        my_list: the given list
    """
    index = len(my_list) - 1
    for i in range(index, -1, -1):
        print("{:d}".format(my_list[i]))
