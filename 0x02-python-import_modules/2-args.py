#!/usr/bin/python3
import sys
if __name__ == '__main__':
    arg_len = len(sys.argv) - 1
    if arg_len == 1:
        print("{} argument:".format(arg_len))
    elif arg_len == 0:
        print("{} arguments.".format(arg_len))
    else:
        print("{} arguments:".format(arg_len))

    for i in range(1, arg_len + 1):
        print("{}: {}".format(i, sys.argv[i]))
