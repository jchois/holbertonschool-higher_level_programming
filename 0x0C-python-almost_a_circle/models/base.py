#!/usr/bin/python3
"""Base"""
from json import dumps, loads


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """init"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation"""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation"""
        newlist = []
        if list_objs is not None:
            for x in range(len(list_objs)):
                newlist += [list_objs[0].to_dictionary()]
            with open(cls.__name__ + ".json", "w") as f:
                f.write(cls.to_json_string(newlist))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation"""
        if json_string is None or not json_string:
            return "[]"
        else:
            return loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        newlist = []
        new_file = cls.__name__ + ".json"
        try:
            with open(new_file, "r") as f:
                newlist = cls.from_json_string(f.read())
            for a, b in enumerate(newlist):
                newlist[a] = cls.create(**newlist[a])
        except:
            pass
        return newlist
