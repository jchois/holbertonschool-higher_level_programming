#!/usr/bin/python3
"""Square class"""


class Square:
    """Private instance attribute declared

    Arguments:
        size: size of a square

    Raises:
        TypeError/ValueError
    """
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
