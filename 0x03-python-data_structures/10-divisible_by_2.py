#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    multi = []
    for ct in range(len(my_list)):
        multi.append(my_list[ct] % 2 == 0)
    return(multi)
