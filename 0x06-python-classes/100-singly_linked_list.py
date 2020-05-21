#!/usr/bin/python3
"""Singly linked list"""


class Node:
    """attribute declared
    Arguments:
        data / next_node
    Raises:
        TypeError
    """
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

        @property
        def data(self):
            return self.__data

        @data.setter
        def data(self, value):
            if type(value) is not int:
                raise TypeError("data must be an integer")
            else:
                self.__data = value

        #New Node
        @property
        def next_node(self):
            return self.__next_node

        @data.setter
        def next_node(self, value):
            if type(value) is Node or None:
                self.__next_node = value
            else:
                raise ("next_node must be a Node object")

"""
Creating a single linked list
"""


class SinglyLinkedList:
    """
    Initialize
    """
    def __init__(self):
        self.__head = None

    """
        Arguments:
            value
    """
    def sorted_insert(self, value):
        tmp = self.__head
        if tmp is None:
            new_node = Node(value, tmp)
            self.__head = new_node
            return

        if tmp.data > value:
            new_node = Node(value, tmp)
            new_node.next_node = tmp
            self.__head = new_node
            return

        while tmp.next_node is not None and tmp.next_node.data < value:
            tmp = tmp.next_node
        new_node = Node(value, tmp)
        new_node.next_node = tmp.next_node
        tmp.next_node = new_node
        return

    """
        string
    """
    def __str__(self):
        tmp = self.__head
        node_list = ""
        while tmp is not None:
            node_list += str(tmp.data)
            tmp = tmp.next_node
            if tmp is not None:
                node_list += "\n"
        return node_list

    """
        repr
    """
    def __repr__(self):
        return self.__str__()
