#!/usr/bin/python3
import hidden_4
if __name__ == '__main__':
    names = dir(hidden_4)
    for e in names:
        if not e.startswith('__'):
            print("{}".format(e))
