#!/usr/bin/python3
"""append_after Module"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file after each line."""
    str = ""
    with open(filename, 'r') as fl:
        for line in fl:
            str += line
            if (search_string in line):
                str += new_string
    with open(filename, 'w') as fl:
        fl.write(str)
