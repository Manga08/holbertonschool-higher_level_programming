#!/usr/bin/python3
def no_c(my_string):
    New_word = ""
    for word in my_string:
        if word != 'c' and word != 'C':
            New_word += word
    return New_word
