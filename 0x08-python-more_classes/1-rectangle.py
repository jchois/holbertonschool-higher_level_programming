#!/usr/bin/python3
"""Rectangle Class"""


class Rectangle:
    def __init__(self, width=0, height=0):
        """[summary]

        Keyword Arguments:
            width {int} -- [description] (default: {0})
            height {int} -- [description] (default: {0})
        """
        self.__width = width
        self.__height = height

    #width
    @property
    def width(self):
        """init width"""
        return self.__width

    @width.setter
    def width(self, value):
        """validates"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    #height
    @property
    def height(self):
        """init height"""
        return self.__height

    @height.setter
    def height(self, value):
        """validates"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
