#!/usr/bin/python3
"""BaseGeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """[Rectangle]

    Arguments:
        BaseGeometry - Inherit
    """
    def __init__(self, width, height):
        """[Init Rectangle]

        Arguments:
            width int
            height int
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
