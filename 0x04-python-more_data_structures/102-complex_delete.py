#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for key, ct in list(a_dictionary.items()):
        if ct is value:
            del a_dictionary[key]
    return a_dictionary
