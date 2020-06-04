#!/usr/bin/python3
"""[Pascal's Triangle ]
"""


def pascal_triangle(n):
    """[pascal_triangle]
    """
    if n <= 0:
        return []
    pascal = []
    row = []
    for i in range(n):
        row = [1]
        if i > 0:
            for j in range(i):
                row.append(sum(pascal[-1][j:j+2]))
        pascal.append(row)
    return pascal
