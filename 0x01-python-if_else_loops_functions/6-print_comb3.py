#!/usr/bin/python3
for n in range(99):
    if n / 10 < n % 10 and n != 89:
        print('{:02d},'.format(n), end=' ')
    elif n == 89:
        print(n)
