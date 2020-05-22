#!/usr/bin/python3
"""Divides a matrix"""


def matrix_divided(matrix, div):
    """Function that divides a matrix"""

    matx = []
    if len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")
    for ct1 in matrix:
        if len(ct1) == 0:
            raise TypeError("matrix must be a matrix (list of lists) "
                            "of integers/floats")
        else:
            matx.append(len(ct1))
        for n in ct1:
            if type(n) is not float and type(n) is not int:
                raise TypeError("matrix must be a matrix (list of lists) "
                                "of integers/floats")
    if len(set(matx)) != 1:
        raise TypeError('Each row of the matrix must have the same size')
    if type(div) is float or type(div) is int:
        pass
    else:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    return [[round(n/div, 2) for n in ct2] for ct2 in matrix]
