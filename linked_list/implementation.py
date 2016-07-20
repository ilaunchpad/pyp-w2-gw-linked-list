from linked_list.interface import AbstractLinkedList
from linked_list.node import Node


class LinkedList(AbstractLinkedList):
    """
    Implementation of an AbstractLinkedList inteface.
    """

    def __init__(self, elements=None):
        self.start = None
        self.end = None
        
        for items in elements:
            if items:
                self.append(items)
        

    def __str__(self):
        pass

    def __len__(self):
        pass

    def __iter__(self):
        pass

    def __getitem__(self, index):
        pass

    def __add__(self, other):
        pass

    def __iadd__(self, other):
        pass

    def __eq__(self, other):
        pass

    def append(self, elem):
        newNode = Node(elem)
        if self.start is None:
            self.start = newNode
            self.end = newNode
        else:
            self.end.next = newNode
            self.end = newNode

    def count(self):
        return len(self)

    def pop(self, index=None):
        pass
 