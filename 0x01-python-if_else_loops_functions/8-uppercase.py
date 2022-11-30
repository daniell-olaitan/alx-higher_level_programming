#!/usr/bin/python3
def is_alpha(c):
    if (ord('a') <= ord(c) <= ord('z')) or (ord('A') <= ord(c) <= ord('Z')):
        return True
    return False

def is_lowercase(c):
    lowest_char = ord('a')
    highest_char = ord('z')
    c = ord(c)
    if lowest_char <= c <= highest_char:
        return True
    return False

def uppercase(str):
    lowest_lowercase = ord('a')
    lowest_uppercase = ord('A')
    difference = lowest_uppercase - lowest_lowercase
    for c in str:
        if is_alpha(c) and is_lowercase(c):
            c = chr(ord(c) + difference)
        print(c, end='')
    print()

uppercase('best')
uppercase('Best oF luCk')
