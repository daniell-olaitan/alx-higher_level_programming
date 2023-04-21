#!/usr/bin/python3
"""
Takes a url, and an e-mail address, sends a post request to it with
the email as the parameter, and displays the body of the response
"""

import requests
from sys import argv


if __name__ == '__main__':
    payload = {'email': argv[2]}
    res = requests.post(argv[1], data=payload)

    print(res.text)
