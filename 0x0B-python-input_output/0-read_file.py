#!/usr/bin/python3
"""function that reads a text file"""


def read_file(filename=""):
    """read_file

    Keyword Arguments:
        filename
    """
    with open(filename, encoding="UTF-8") as myFile:
        print(myFile.read())
