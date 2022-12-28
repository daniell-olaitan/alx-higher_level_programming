#!/usr/bin/python3
"""contains a class 'Node' that defines a node of a singly linked list
   and another that defines the List
"""


class Node:
    """Defines a node of a singly linked list
    """
    def __init__(self, data, next_node=None):
        """initializes the private attributes
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """sets and retrieves 'data' instance attribute
        """
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is int:
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        """sets and retrieves the next node of the list
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is None or type(value) is Node:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """Defines a singly linked list
    """
    def __init__(self):
        """Sets the head of the list to None
        """
        self.__head = None

    def __str__(self):
        current = self.__head
        res = []
        while current is not None:
            res.append(str(current.data))
            current = current.next_node

        return '\n'.join(res)

    def sorted_insert(self, value):
        """Inserts a node into the list in a sorted increasing order

        Args:
            value: the value of the data to be inserted
        """
        node = Node(value)
        current = self.__head
        prev = self.__head
        while current is not None:
            if current.data >= value:
                if current is self.__head:
                    node.next_node = self.__head
                    self.__head = node
                else:
                    node.next_node = current
                    prev.next_node = node

                break

            prev = current
            current = current.next_node
        else:
            if self.__head is None:
                self.__head = node
            else:
                prev.next_node = node
