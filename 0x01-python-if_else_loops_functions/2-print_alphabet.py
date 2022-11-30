#!/usr/bin/python3
asci = ord('a')
while True:
    alphabet = chr(asci)
    print(alphabet, end="")
    if alphabet == 'z':
        break
    asci = asci + 1
