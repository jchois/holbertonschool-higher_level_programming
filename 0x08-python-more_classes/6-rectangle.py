#!/usr/bin/python3
"""Rectangle Class"""


class Rectangle:
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """[summary]

        Keyword Arguments:
            width {int} -- [description] (default: {0})
            height {int} -- [description] (default: {0})
        """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    # width
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

    # height
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

    def area(self):
        """area func"""
        return self.width * self.height

    def perimeter(self):
        """perimeter func"""
        if self.width == 0 or self.height == 0:
            return 0
        return (2 * (self.width + self.height))

    def __str__(self):
        """str"""
        if self.width == 0 or self.height == 0:
            return ("")
        width = "#" * self.width
        show = width
        for i in range(0, self.height - 1):
            show += "\n" + width
        return show

    def __repr__(self):
        """repr"""
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """del"""
        if Rectangle.number_of_instances > 0:
            Rectangle.number_of_instances -= 1
            print("{}".format("Bye rectangle..."))
