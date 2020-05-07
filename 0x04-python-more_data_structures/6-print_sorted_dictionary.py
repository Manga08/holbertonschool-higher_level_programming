#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for ct in sorted(a_dictionary):
        print("{}: {}".format(ct, a_dictionary[ct]))
