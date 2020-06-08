#!/usr/bin/python3
"""Rectangle that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    #width
    @property
    def width(self):
        """getter - with"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter - width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    #height
    @property
    def height(self):
        """getter - height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter - height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    #x
    @property
    def x(self):
        """getter - x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter - x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    #y
    @property
    def y(self):
        """getter - y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter - y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        '''This is the area operation.'''
        return (self.__width * self.__height)

    def display(self):
        """Print a rectangle with #"""
        for new in range(self.y):
            print()
        for i in range(self.height):
            for space in range(self.x):
                print(" ", end="")
            for w in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """Return [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args):
        """Assigns an argument to each attribute"""
        for a, b in enumerate(args):
            if a == 0:
                self.id = b
            if a == 1:
                self.width = b
            if a == 2:
                self.height = b
            if a == 3:
                self.x = b
            if a == 4:
                self.y = b
