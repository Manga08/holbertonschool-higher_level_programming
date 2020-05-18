#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    numb = 0
    for ct in range(x):
        try:
            print("{:d}".format(my_list[ct]), end="")
            numb += 1
        except (ValueError, TypeError):
            continue
    print()
    return numb
