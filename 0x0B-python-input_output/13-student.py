#!/usr/bin/python3
"""Student Class"""


class Student:
    """Class Student"""

    def __init__(self, first_name, last_name, age):
        """initialize"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """to_json"""
        new = {}
        if attrs is None:
            return self.__dict__
        for i in attrs:
            if hasattr(self, i):
                new[i] = getattr(self, i)
        return new

    def reload_from_json(self, json):
        """reload"""
        for x, y in json.items():
            if hasattr(self, i):
                setattr(self, x, y)
