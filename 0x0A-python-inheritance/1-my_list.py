#!/usr/bin/python3
"""Mylist Class"""


class MyList(list):
    """Inherits from list."""

    def print_sorted(self):
        """Prints the list, but sorted."""
        print(sorted(self))