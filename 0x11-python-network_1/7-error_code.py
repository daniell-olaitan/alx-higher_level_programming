#!/usr/bin/python3
"""
Takes a url, sends a request to the url, and displays the
body of the response
"""

from sys import argv
import requests


if __name__ == '__main__':
    res = requests.get(argv[1])
    if res.status_code >= 40:
        print('Error code:', res.status_code)
    else:
        print(res.text)
