#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """Prints 'x' number of elements from a list

    Args:
        my_list: the given list (of any type)
        x: number of elements to print (can be more than len of list)

    Return: the actual number of elements printed
    """
    num_of_element = 0
    for i in range(0, x):
        try:
            print(my_list[i], end="")
            num_of_element += 1
        except IndexError:
            break

    print()
    return num_of_element
