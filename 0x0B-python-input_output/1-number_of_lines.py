#!/usr/bin/python3
"""Function that returns the number of lines of a text file"""


def number_of_lines(filename=""):
    """Return number of lines"""
    count = 0
    with open(filename) as myFile:
        while myFile.readline():
            count += 1
    return count
