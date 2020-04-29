#!/usr/bin/python3
def remove_char_at(str, c):
    if c < 0:
        return(str)
    return(str[0:c] + str[c + 1:])
