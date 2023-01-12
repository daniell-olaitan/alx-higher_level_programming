#!/usr/bin/python3
"""modules adds args to a list and save them to a filee"""
import sys

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

if __name__ == '__main__':
    filename = "add_item.json"
    try:
        res = load_from_json_file(filename)
    except FileNotFoundError:
        res = []

    save_to_json_file(res + sys.argv[1:], filename)
