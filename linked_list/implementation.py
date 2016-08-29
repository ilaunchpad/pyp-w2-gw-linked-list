from .interface import AbstractLinkedList
from node import *

class LinkedList(AbstractLinkedList):
    """
    Implementation of an AbstractLinkedList inteface.
    """

    def __init__(self, elements=None):
        self.start = None
        self.end = None
        self.count_ = 0
        if elements == None:
            return
        for element in elements:
            self.append(element)
        pass

    def __str__(self):
       current = self.start
       ans = "["
       while current != None:
           ans += str(current.elem)
           if current.next !=None:
               ans +=", "
           current = current.next
       ans += "]"
       return ans


    def __len__(self):
        return self.count_


    def __iter__(self):
        current = self.start
        while current !=None:
            yield current.elem
            current = current.next

    def __getitem__(self, index):
        if index >= self.count_:
            raise IndexError
        for i, node in enumerate(self):
            if i == index:
                return node



    def __add__(self, other):
        ans = LinkedList(self)
        ans += other
        return ans


    def __iadd__(self, other):
        if other == None:
           return self
        for node in other:
            self.append(node)
        return self

    def __eq__(self, other):
        if other == None:
            return False
        if len(self) != len(other):
            return False
        length = len(self)
        for i in range(length):
            if self[i] != other[i]:
                return False
        return True


    def append(self, elem):
        node = Node(elem)
        if self.count_ == 0:  # first_element
            self.start = node
            self.end = node
            self.end.next = None
        else:
            self.end.next = node
            self.end = self.end.next
        self.count_ += 1


    def count(self):
        return len(self)

    def pop(self, index=None):
        ans = None
        if index is None:
            index = len(self) - 1
        if index < 0 or index >= len(self):
            raise IndexError
        self.count_ -= 1
        if index == 0:
            ans = self.start
            self.start = self.start.next
            return ans.elem
        i = 0
        current = self.start
        while i < index - 1:
            current = current.next
            i += 1
        ans = current.next
        current.next = current.next.next
        return ans.elem

    def __ne__(self, other):
        return not self == other


