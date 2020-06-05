#!/usr/bin/python3
"""x"""


def read_lines(filename="", nb_lines=0):
    """x"""
    with open(filename, "r", encoding="UTF-8") as myFile:
        count = 0
        for i in open(filename):
            count += 1
        if nb_lines <= 0 or nb_lines >= count:
            print(myFile.read(), end="")
        else:
            for i in range(nb_lines):
                print(myFile.readline(), end="")
