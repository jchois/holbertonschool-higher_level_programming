#!/usr/bin/python3
"""Square class module
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square

    Args:
        Rectangle ([class]): class Square that inherits from Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """initialize method

        Args:
            size ([int]): [size of square]
            x (int, optional): number of spaces. Defaults to 0.
            y (int, optional): number of \n. Defaults to 0.
            id ([int], optional): id. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """str method

        Returns:
            str: Returns string info about this square.
        """
        return "[{}] ({}) {}/{} - {}".format(
            type(self).__name__,
            self.id, self.x,
            self.y,
            self.width
        )

    @property
    def size(self):
        """size getter
        """
        return self.width

    @size.setter
    def size(self, value):
        """size setter
        """
        self.width = value
        self.height = value

    def arg_update(self, id=None, size=None, x=None, y=None):
        """arg_update - upgrade instance attribute via *args
        """
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
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
        return {"id": self.id, "x": self.x, "size": self.size, "y": self.y}
