#!/usr/bin/python3
"""Function that Read n number of lines."""


def read_lines(filename="", nb_lines=0):
    """Function that reads the file that the user needs."""
    with open(filename, 'r') as fl:
        if nb_lines <= 0:
            print(fl.read(), end='')
            return
        ct = 0
        for line in fl:
            if ct < nb_lines:
                print(line, end='')
            ct += 1
