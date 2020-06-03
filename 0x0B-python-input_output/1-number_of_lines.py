#!/usr/bin/python3
"""Numbers of line function"""


def number_of_lines(filename=""):
    """Count the number of lines in a text file and print it."""
    ct = 0
    with open(filename, 'r') as fl:
        for line in fl:
            ct += 1
    return ct
