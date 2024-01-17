#!/usr/bin/python3
"""
Takes a url, sends a request and displays the body of the
response
"""

from sys import argv
from urllib.request import Request, urlopen
from urllib.error import HTTPError


if __name__ == '__main__':
    req = Request(argv[1])
    try:
        with urlopen(req) as response:
            content = response.read().decode('utf-8')
            print(content)
    except HTTPError as e:
        print("Error code: {}".format(e.code))
