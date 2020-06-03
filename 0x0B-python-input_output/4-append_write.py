#!/usr/bin/python3
"""Function that append a string."""


def append_write(filename="", text=""):
    """Append a string to a file"""
    with open(filename, 'a') as fl:
        return fl.write(str(text))
