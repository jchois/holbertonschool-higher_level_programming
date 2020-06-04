#!/usr/bin/python3
"""x"""


def read_lines(filename="", nb_lines=0):
    """x"""
    with open(filename, "r", encoding="UTF-8") as myFile:
        count = 0
        if nb_lines <= 0:
            print(myFile.read(), end="")
        
