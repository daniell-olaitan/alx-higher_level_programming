#!/usr/bin/python3
"""contains a function that reads and prints a file"""


def read_file(filename=""):
    """reads a text file (UTF8) and prints it to stdout

    Args:
        filename: name of file
    """
    if filename:
        with open(filename, 'r', encoding='utf-8') as f:
            print(f.read())
