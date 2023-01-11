#!/usr/bin/python3
"""contains a function that writes an obj's json rep to a text file"""
import json


def save_from_json_file(my_obj, filename):
    """writes an Object to a text file"""
    if filename:
        with open(filename, 'w', encoding="utf-8") as fd:
            json.dump(my_obj, fd)
