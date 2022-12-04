#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """Adds two tuples

    Args:
        tuple_a: the first tuple
        tuple_b: the second tuple

    Returns:
        a tuple with two integers
    """
    copy = [[0, 0], [0, 0]]
    tuples = [tuple_a, tuple_b]
    for i, tuple_ in enumerate(tuples):
        tuple_len = len(tuple_)
        if tuple_len == 1:
            copy[i][0] = tuple_[0]
        elif tuple_len != 0:
            copy[i][0] = tuple_[0]
            copy[i][1] = tuple_[1]

    sum_a = copy[0][0] + copy[1][0]
    sum_b = copy[0][1] + copy[1][1]
    return sum_a, sum_b
