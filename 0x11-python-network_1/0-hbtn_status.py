#!/usr/bin/python3
"""Fetches a url and displays the body of the response"""

from urllib.request import Request, urlopen


if __name__ == '__main__':
    req = Request('https://alx-intranet.hbtn.io/status')
    with urlopen(req) as response:
        content = response.read()

        print("Body response:")
        print(f"\t- type: {type(content)}")
        print(f"\t- content: {content}")
        print("\t- utf8 content: {}".format(content.decode('utf-8')))
