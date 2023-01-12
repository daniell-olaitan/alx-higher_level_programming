#!/usr/bin/python3
"""contains a func that inserts a line of text to a file"""
import json


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file after each line containing
       a special string

    Args:
        filename: path to text file
        search_string: special string
        new_string: string to insert
    """
    lines = []
    if filename and search_string
        with open(filename, "r", encoding="utf-8") as fd:
            lines += fd.readlines()

        with open(filename, "w", encoding="utf-8") as fd:
            for line in lines:
                fd.write(line)
                if search_string in line:
                    fd.write(new_string)
