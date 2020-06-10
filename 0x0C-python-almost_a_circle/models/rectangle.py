#!/usr/bin/python3
"""Rectangle class module

Raises:
    TypeError: [width must be an integer]
    ValueError: [width must be > 0]
    TypeError: [height must be an integer]
    ValueError: [height must be > 0]
    TypeError: [x must be an integer]
    ValueError: [x must be >= 0]
    TypeError: [y must be an integer]
    ValueError: [y must be >= 0]
"""
from models.base import Base


class Rectangle(Base):
    """Class Rectangle

    Args:
        Base (Class): [Class Rectangle inherits from Base]
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """initialize module

        Args:
            width (int): width
            height (int): height
            x (int): x. Defaults to 0.
            y (int): y. Defaults to 0.
            id ([type], optional): id. Defaults to None.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """width getter
        """
        return self.__width

    @width.setter
    def width(self, width):
        """width setter

        Args:
            width (int): width

        Raises:
            TypeError: [width must be an integer]
            ValueError: [width must be > 0]
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """height getter
        """
        return self.__height

    @height.setter
    def height(self, height):
        """height setter

        Args:
            height (int): height

        Raises:
            TypeError: [height must be an integer]
            ValueError: [height must be > 0]
        """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """x getter
        """
        return self.__x

    @x.setter
    def x(self, x):
        """x setter

        Args:
            x (int)

        Raises:
            TypeError: [x must be an integer]
            ValueError: [x must be >= 0]
        """
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """y getter
        """
        return self.__y

    @y.setter
    def y(self, y):
        """y setter

        Args:
            y (int)

        Raises:
            TypeError: [y must be an integer]
            ValueError: [y must be >= 0]
        """
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """area method

        Returns:
            [int]: [area of a rectangle]
        """
        return self.__height * self.__width

    def display(self):
        """display method
        """
        s = '\n' * self.y + \
            (' ' * self.x + '#' * self.width + '\n') * self.height
        print(s, end='')

    def __str__(self):
        """str method

        Returns:
            str: Returns string info about this rectangle.
        """
        return "[{}] ({}) {}/{} - {}/{}".format(
            type(self).__name__,
            self.id,
            self.x,
            self.y,
            self.width,
            self.height
        )

    def arg_update(self, id=None, width=None, height=None, x=None, y=None):
        """arg_update - upgrade instance attribute via *args
        """
        if id is not None:
            self.id = id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """update method
        """
        if args:
            self.arg_update(*args)
        elif kwargs:
            self.arg_update(**kwargs)

    def to_dictionary(self):
        """to_dictionary method

        Returns:
            [dict]: dictionary representation of this class
        """
        return {"x": self.x, "y": self.y, "id": self.id,
                "height": self.height, "width": self.width}
