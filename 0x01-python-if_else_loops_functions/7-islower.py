#!/usr/bin/python3
def islower(c):
    lowest_char = ord('a')
    highest_char = ord('z')
    c = ord(c)
    if lowest_char <= c <= highest_char:
        return True
    return False
