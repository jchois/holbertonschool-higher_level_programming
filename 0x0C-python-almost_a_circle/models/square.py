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
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width, self.height)
