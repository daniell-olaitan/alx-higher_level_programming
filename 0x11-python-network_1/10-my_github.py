#!/usr/bin/python3
"""
Takes github credentials and displays the github id
"""

import requests
from requests.auth import HTTPBasicAuth
from sys import argv

if __name__ == '__main__':
    url = 'https://api.github.com/user'
    auth = HTTPBasicAuth(argv[1], argv[2])
    res = requests.get(url, auth=auth)
    print(res.json().get('id'))
