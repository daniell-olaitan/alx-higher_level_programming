#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """Divides elements from list 1 by those of list 2

    Args:
        my_list_1: list 1
        my_list_2: list 2
        list_length: length of new list

    Returns:
        a list of the divisions
    """
    res = []
    for i in range(0, list_length):
        try:
            a = float(my_list_1[i])
            b = float(my_list_2[i])
            result = a / b
        except (ValueError, TypeError):
            print("wrong type")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        finally:
            res.append(result)

    return res
