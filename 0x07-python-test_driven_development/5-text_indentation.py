#!/usr/bin/python3
"""Prints a text with 2 new lines"""


def text_indentation(text):
    """Prints 2 new lines after this characters: ., ? and :"""

    if type(text) is not str:
        raise TypeError('text must be a string')

    new_ln = True
    for ct in text:
        if not (new_ln and ct == ' '):
            print(ct, end='')
            new_ln = False
            if ct in '.?:':
                print('\n')
                new_ln = True
