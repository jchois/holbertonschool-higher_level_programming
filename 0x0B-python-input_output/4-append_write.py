#!/usr/bin/python3
"""function that appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """appends a string at the end of the file"""
    with open(filename, "a", encoding="UTF-8") as myFile:
        return myFile.write(text)
