#!/usr/bin/python3
def remove_char_at(string, x):
    if (x >= 0):
        return string[:x] + string[x + 1:]
    else:
        return string
