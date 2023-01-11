#!/usr/bin/python3
"""module contains a function that appends to a file"""


def append_write(filename"", text=""):
    """appends a string at the end of a text file (utf8)

    Args:
        filename: name of file
        text: string to append

    return:
        the number of characters appended
    """
    if filename:
        with open(filename, 'a', encoding="utf-8") as append_file:
            return append_file.write(text)
