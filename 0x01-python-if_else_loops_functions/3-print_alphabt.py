#!/usr/bin/python3
asci = ord('a')
while True:
    alphabet = chr(asci)
    if alphabet == 'q' or alphabet == 'e':
        asci = asci + 1
        continue
    print("{}".format(alphabet), end="")
    if alphabet == 'z':
        break
    asci = asci + 1
