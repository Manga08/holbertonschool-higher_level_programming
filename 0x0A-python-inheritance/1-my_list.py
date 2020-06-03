#!/usr/bin/python3
""" Module of MyList"""


class MyList(list):
    """Class MyList"""
    def print_sorted(self):
        """Prints the list"""
        print(sorted(self))
