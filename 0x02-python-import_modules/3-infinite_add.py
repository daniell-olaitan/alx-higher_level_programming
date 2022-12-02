#!/usr/bin/python3
from sys import argv
if __name__ == '__main__':
    summ = 0
    length = len(argv)
    for i in range(1, length):
        summ = summ + int(argv[i])

    print("{}".format(summ))
