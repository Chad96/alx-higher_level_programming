#!/usr/bin/python3
"""Define a singly linked list"""


class Node:
    """Class that defines a node of a singly linked list"""

    def __init__(self, data, next_node=None):
        """Initialization method with data and next_node parameters"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter method to retrieve the data attribute"""
        return self.__data

    @data.setter
    def data(self, value):
        """Setter method to set the data attribute"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")

        self.__data = value

    @property
    def next_node(self):
        """Getter method to retrieve the next_node attribute"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Setter method to set the next_node attribute"""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")

        self.__next_node = value


class SinglyLinkedList:
    """Class that defines a singly linked list"""

    def __init__(self):
        """Initialization method for the singly linked list"""
        self.head = None

    def sorted_insert(self, value):

        new_node = Node(value)

        if self.head is None or self.head.data >= value:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node and current.next_node.data < value:
                current = current.next_node

                new_node.next_node = current.next_node
                current.next_node = new_node

    def __str__(self):
        """String representation of the singly linked list"""
        result = ""
        current = self.head
        while current:
            result += str(current.data) + "\n"
            current = current.next_node

        return result.strip()
