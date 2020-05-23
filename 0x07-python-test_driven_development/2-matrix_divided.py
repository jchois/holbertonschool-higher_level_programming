#!/usr/bin/python3
"""
Function that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """[matrix_divided]
    Arguments:
        matrix  -- [matrix]
        div -- [indenx to divide]
    """
    merror = "matrix must be a matrix (list of lists) of integers/floats"
    if type(div) not in [int, float]:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    try:
        row = matrix[1][0]
    except TypeError:
        return (merror)
    new_matrix = []
    length_matrix = len(matrix[0])

    for row in matrix:
        n_row = []
        if type(row) is not list:
            raise TypeError(merror)
        if length_matrix != len(row):
            raise TypeError('Each row of the matrix must have the same size')
        for element in row:
            if type(element) not in [int, float]:
                raise TypeError(merror)
            n_row.append(round(element / div, 2))
        new_matrix.append(n_row)
    return new_matrix
