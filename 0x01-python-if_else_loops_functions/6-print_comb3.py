#!/usr/bin/python3
for x in range(10):
    for y in range(10):
        if x < y:
            print('{:d}{:d}{:s}'.format(
                x, y, '\n' if (x == 8) and (y == 9) else ', '), end='')
