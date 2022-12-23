#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """Prints the first 'x' elements of a list and only ints

    Args:
        my_list: the given lists
        x: the number of elements to access in my_list

    Return:
        the number of ints printed
    """
    num_of_ints = 0
    for i in range(0, x):
        try:
            print("{:d}".format(int(my_list[i])), end="")
            num_of_ints += 1
        except (ValueError, TypeError):
            continue

    print()
    return num_of_ints
