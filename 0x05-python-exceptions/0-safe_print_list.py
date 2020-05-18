#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    numb = 0
    for ct in range(x):
        try:
            print('{}'.format(my_list[ct]), end="")
            numb += 1
        except IndexError:
            break
    print()
    return numb
