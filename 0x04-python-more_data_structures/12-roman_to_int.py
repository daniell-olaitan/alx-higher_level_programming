#!/usr/bin/python3
def roman_to_int(roman_string):
    """Converts roman numeral to integer

    Args:
        roman_string: the given roman numeral

    Return:
        the converted integer
    """
    digits = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    res = []

    for i in roman_string:
        if i in digits:
            value = digits[i]
            if res:
                if res[-1] < value:
                    res[-1] = value - res[-1]
                else:
                    res.append(value)
            else:
                res.append(value)

    return sum(res)
