#!/usr/bin/python3
"""pascal_triangle Module"""


def pascal_triangle(n):
    """Returns a list of lists of integers representing the Pascal triangle."""
    my_list = []
    if n <= 0:
        return my_list

    for ct1 in range(1, n + 1):
        numb = 1
        temp = []
        for ct2 in range(1, ct1 + 1):
            temp.append(str(numb))
            numb = numb * (ct1 - ct2) // ct2
        my_list.append(temp)
    return my_list
