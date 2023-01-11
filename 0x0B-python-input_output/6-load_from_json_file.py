#!/usr/bin/python3
"""contains a function that crates an object from a json file"""
import json


def load_from_json_file(filename):
    """creates and returns an object from a JSON file"""
    if filename:
        with open(filename, "r", encoding="utf-8") as json_file:
            return json.load(json_file)
