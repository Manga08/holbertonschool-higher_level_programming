#!/usr/bin/python3
"""Node And SinglyLinkedList Class"""


class Node:
    """A Node class that define the next node and the data"""

    def __init__(self, data, next_node=None):
        """Initializes the data and the next value"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get the data"""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data."""
        if type(value) != int:
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        """Get the next node value"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next node of the list and set the error"""
        if type(value) != Node and value is not None:
            raise TypeError('next_node must be a Node object')
        self.__next_node = value


class SinglyLinkedList:
    """A SinglyLinkedList class that define a linket list"""

    def __init__(self):
        """Initialize the head of the list"""
        self.head = None

    def __repr__(self):
        """Initialize the string and the current position"""
        string = ''
        current = self.head
        while current:
            string += str(current.data) + '\n'
            current = current.next_node
        return string[:-1]

    def sorted_insert(self, value):
        """Add a new node sorted in the correct position"""
        new_node = Node(value)
        current = self.head
        if current is None:
            self.head = new_node
            return
        if current.data > value:
            new_node.next_node = self.head
            self.head = new_node
            return
        while current.next_node is not None:
            if current.next_node.data > value:
                break
            current = current.next_node
        new_node.next_node = current.next_node
        current.next_node = new_node
        return
