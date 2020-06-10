#!/usr/bin/python3
"""model Base"""
from json import dumps, loads


class Base:
    """Class Base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """to_json_string method
        Args:
            list_dictionaries ([int]):  is a list of dictionaries
        Returns:
            [JSON]: Return the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save to file method

        Args:
            list_objs ([int])
        """
        new_lst = []
        if list_objs is not None:
            for x in range(len(list_objs)):
                new_lst += [list_objs[x].to_dictionary()]
        with open(cls.__name__ + ".json", 'w') as f:
            f.write(cls.to_json_string(new_lst))

    @staticmethod
    def from_json_string(json_string):
        """from json to string

        Args:
            json_string ([type]): [description]

        Returns:
            [type]: [description]
        """
        if json_string is None or not json_string:
            return []
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
        """load_from method

        Returns:
            [list]: list of instance
        """
        new_file = cls.__name__ + ".json"
        new_lst = []
        try:
            with open(new_file, 'r') as f:
                new_lst = cls.from_json_string(f.read())
            for a, _b in enumerate(new_lst):
                new_lst[a] = cls.create(**new_lst[a])
        except:
            pass
        return new_lst
