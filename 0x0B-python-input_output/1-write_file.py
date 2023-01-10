#!/usr/bin/python3
"""contains a function that writes a string to a file"""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8)

    Args:
        filename: name of file
        text: string to write to file

    Return:
        number of characters written to file
    """
    if filename:
        with open(filename, 'w', encoding='utf-8') as writeFile:
            return writeFile.write(text)
