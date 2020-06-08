#!/usr/bin/python3
"""Square that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Squeare class"""
    def __init__(self, size, x=0, y=0, id=None):
        """init constructor"""
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """Return [Square] (<id>) <x>/<y> - <size>"""
        return "[Square] ({}) {}/{} - {}\
            ".format(self.id, self.x, self.y, self.width)

    # size
    @property
    def size(self):
        """getter - size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter - size"""
        self.width = value
        self.height = value

    def update_args(self, id=None, size=None, x=None, y=None):
        """upgrade instance attribute via *args"""
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""
        if args:
            self.update_args(*args)
        elif kwargs:
            self.update_args(**kwargs)

    def to_dictionary(self):
        """returns the dictionary representation"""
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
