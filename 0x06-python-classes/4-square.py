#!/usr/bin/python3
"""Access and update private attribute"""


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

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    """
        Function that returns the current square area
    """
    def area(self):
        return self.__size ** 2
