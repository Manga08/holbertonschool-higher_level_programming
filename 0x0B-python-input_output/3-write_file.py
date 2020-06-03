#!/usr/bin/python3
"""Function that write in a file."""


def write_file(filename="", text=""):
    """Write a string in a text file."""
    with open(filename, 'w') as fl:
        return fl.write(str(text))
