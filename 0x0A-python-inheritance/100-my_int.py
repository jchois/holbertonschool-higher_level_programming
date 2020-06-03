#!/usr/bin/python3
"""MyInt class"""


class MyInt(int):
    def __init__(self, value):
        """init"""
        self.value = value

    def __eq__(self, other):
        """override =="""
        return self.value != other

    def __ne__(self, other):
        """override !="""
        return self.value == other
