#!/usr/bin/python3
"""Coordinates of a square"""


class Square:
    """Private instance attribute declared
    Arguments:
        size: size of a square
    Raises:
        TypeError/ValueError
    """
    def __init__(self, size=0, position=(0, 0)):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not int or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    """
        Function that returns the current square area
    """
    def area(self):
        return self.__size ** 2

    """
        Function that prints in stdout the square
    """
    def my_print(self):
        self.row = 0
        if self.size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print()
            while self.row < self.size:
                print("{}{}".format(" " * self.position[0], "#" * self.size))
                self.row += 1
