#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        index = 0
        for element in row:
            if index < len(row) - 1:
                print("{:d} ".format(element), end='')
            else:
                print("{:d}".format(element), end='')
            index = index + 1
        print("")
