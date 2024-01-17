#!/usr/bin/python3
"""
Takes in a URL and an email, sends a post request to the url
with the email as the parameter
"""

from sys import argv
from urllib.request import Request, urlopen
from urllib.parse import urlencode


if __name__ == '__main__':
    value = {'email': argv[2]}
    data = urlencode(value).encode('ascii')
    req = Request(argv[1], data)
    with urlopen(req) as response:
        content = response.read().decode('utf-8')
        print(content)
