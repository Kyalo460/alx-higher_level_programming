"""In this module I will create two classes
one class will create a Node and the other
will create a linked list.
"""


class Node:
    """The class responsible for creating a Node."""
    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if type(value) not in [None, Node]:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """This class will be responsible for printing lists
    and inserting new nodes.
    """

    def __init__(self):
        self.__head = None

    def __repr__(self):
        if self.__head is None:
            return ''
        currentNode = self.__head
        string = ''
        while currentNode:
            string += str(currentNode.data)
            if currentNode.next_node:
                string += '\n'
            currentNode = currentNode.next_node

        return string

    def sorted_insert(self, value):
        """Adds a new node at a position dependant on it's value.
        If new node's value is smaller then it gets added higher in the list.
        """
        newNode = Node(value)

        if self.__head is None:
            self.__head = newNode
        else:
            if self.__head.data > newNode.data:
                newNode.next_node = self.__head
                self.__head = newNode

            else:
                currentNode = self.__head
                while currentNode is not None:
                    if currentNode.next_node:
                        if currentNode.next_node.data > newNode.data:
                            newNode.next_node = currentNode.next_node
                            currentNode.next_node = newNode
                            break
                    else:
                        currentNode.next_node = newNode
                        break
                    currentNode = currentNode.next_node
