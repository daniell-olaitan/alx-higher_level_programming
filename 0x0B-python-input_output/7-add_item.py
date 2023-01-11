#!/usr/bin/python3
"""modules adds args to a list and save them to a filee"""
from sys import argv
import json

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

filename = "add_item.json"
res = load_from_json_file(filename)
save_to_json_file(res + argv[1:], filename)
