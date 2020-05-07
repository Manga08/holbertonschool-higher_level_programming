#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    New_matrix = []
    for ct in matrix:
        New_matrix.append(list(map(lambda ct: ct ** 2, ct)))
    return New_matrix
