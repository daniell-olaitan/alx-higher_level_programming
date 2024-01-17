#!/usr/bin/python3
"""
Takes a letter and sends a post request with the letter as a parameter
"""

from sys import argv
import requests


if __name__ == '__main__':
    q = "" if len(argv) < 2 else argv[1]
    payload = {'q': q}
    url = 'http://0.0.0.0:5000/search_user'
    try:
        res = requests.post(url, data=payload).json()
        if not res:
            print('No result')
        else:
            print("[{}] {}".format(res.get('id'), res.get('name')))
    except ValueError:
        print('Not a valid JSON')
