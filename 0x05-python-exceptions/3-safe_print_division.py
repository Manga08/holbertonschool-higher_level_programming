#!/usr/bin/python3
def safe_print_division(a, b):
    numb = None
    try:
        numb = a / b
    except ZeroDivisionError:
        return None
    finally:
        print("Inside result: {}".format(numb))
    return numb
