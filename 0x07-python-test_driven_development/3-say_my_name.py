#!/usr/bin/python3
"""Say my name"""


def say_my_name(first_name, last_name=""):
    """[summary]

    Arguments:
        first_name {[type]} -- [description]

    Keyword Arguments:
        last_name {str}

    Raises:
        TypeError: must be a string
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    elif type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
