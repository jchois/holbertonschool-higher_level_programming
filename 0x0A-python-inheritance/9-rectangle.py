#!/usr/bin/python3
"""BaseGeometry"""


class BaseGeometry:
    """empty class"""
    pass

    def area(self):
        """[area]

        Raises:
            Exception: [area() is not implemented]
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """[summary]

        Arguments:
            name / value

        Raises:
            TypeError: <name> must be grater than 0
            ValueError: <name> must be an integer
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """[Rectangle]

    Arguments:
        BaseGeometry - Inherit
    """
    def __init__(self, width, height):
        """init

        Arguments:
            width int
            height int
        """
        self.__width = width
        self.__height = height
        Rectangle.integer_validator(self, "width", width)
        Rectangle.integer_validator(self, "height", height)

    def __str__(self):
        """Return the print() and str() representation of a Rectangle"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string

    def area(self):
        """return area of rectangle"""
        return self.__width * self.__height
