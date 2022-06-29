#!/usr/bin/python3
for x in range(ord('z'), ord('a') - 1, -1):
    if x % 2 == 1:
        x = x - 32
    print("{:s}".format(chr(x)), end="")
