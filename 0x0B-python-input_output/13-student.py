#!/usr/bin/python3
"""[Student to JSON with filter]
"""


class Student:
    """[Student]
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        dic = {}
        if attrs is None:
            return self.__dict__
        for i in attrs:
            if hasattr(self, i):
                dic[i] = getattr(self, i)
        return dic

    def reload_from_json(self, json):
        for i, j in json.items():
            if hasattr(self, i):
                setattr(self, i, j)
