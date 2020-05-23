#!/usr/bin/python3
"""Integers addition"""


def add_integer(a, b=98):
    """[summary]

    Arguments:
        a {[type]} -- [description]

    Keyword Arguments:
        b {int} -- [description] (default: {98})

    Raises:
        TypeError: [description]
        TypeError: [description]

    Returns:
        [type] -- [description]
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    elif type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
