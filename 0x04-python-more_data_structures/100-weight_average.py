#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0

    op = 0
    weight = 0

    for num in my_list:
        op += num[0] * num[1]
        weight += num[1]
    return (op / weight)
