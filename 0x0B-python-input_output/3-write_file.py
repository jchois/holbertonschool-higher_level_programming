#!/usr/bin/python3
"""function that writes a string to a text file"""


def write_file(filename="", text=""):
    """writes a string to a text file"""
    with open(filename, "w", encoding="UTF-8") as myFile:
        return myFile.write(text)
