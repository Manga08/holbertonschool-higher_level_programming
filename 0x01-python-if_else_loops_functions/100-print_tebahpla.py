#!/usr/bin/python3
for letters in reversed(range(97, 123)):
    if letters % 2 != 0:
        letters = letters - 32
    print('{}'.format(chr(letters)), end='')
