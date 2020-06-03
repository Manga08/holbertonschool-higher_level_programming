#!/usr/bin/python3
"""Function that reads a file"""


def read_file(filename=""):
    """Reads a text of a file."""
    with open(filename, 'r') as fl:
        print(fl.read(), end="")
