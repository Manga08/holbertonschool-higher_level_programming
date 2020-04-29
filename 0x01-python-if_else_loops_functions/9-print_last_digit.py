#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        lastd = number % -10
        lastd = -lastd
    else:
        lastd = number % 10
    print("{:d}".format(lastd), end="")
    return(lastd)
