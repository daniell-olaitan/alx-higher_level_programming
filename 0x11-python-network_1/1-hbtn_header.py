#!/usr/bin/python3
"""
Takes in a url, sends a request to the url  and displays the value
of the X-Request-Id variable found in the header of the response
"""

from sys import argv
from urllib.request import Request, urlopen


if __name__ == '__main__':
    req = Request(argv[1])
    with urlopen(req) as response:
        headers = response.info()
        print(headers.get('X-Request-Id'))
