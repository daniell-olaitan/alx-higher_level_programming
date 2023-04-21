#!/usr/bin/python3
"""
Takes a url, sends a request to it and displays the value of a header variable
"""

from sys import argv
import requests


if __name__ == '__main__':
    res = requests.get(argv[1])

    print(res.headers.get('X-Request-Id'))
