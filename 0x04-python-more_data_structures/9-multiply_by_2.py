#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_numb = {}
    for key in a_dictionary:
        temp = a_dictionary[key] * 2
        new_numb[key] = temp
    return new_numb
