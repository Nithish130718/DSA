'''
This module provides an Abstract Base Class named 'AbstractBinaryTree' that provides a few abstract methods and concrete methods for the implementation of
a Tree ADT.

The code is purely based on my logic and might have some errors or bugs. 
Kindly feel free for any corrections or suggestions.

Author: Nithish Kumar S [3122 22 5002 084]

Created on: 28th June 2023

Revised on: 28th June 2023 
'''

from abc import ABC, abstractmethod
from AbstractTree import AbstractTree


class AbstractBinaryTree(AbstractTree):
    '''
    This class is a Abstract Base class for a BinaryTree ADT.
    It has the following methods:
        1) Abstract methods such as 'left','right'.
        2) Concrete methods such as:
            (i) A method 'children' to return the address of child nodes of a node.
            (ii) A method 'siblings' to return the sibling address of a node.
    '''

    @abstractmethod
    def left(self,pos):
        pass


    @abstractmethod
    def right(self,pos):
        pass


    def children(self,pos):
        if pos is None:
            return None
        if self.left(pos) is not None:
            yield self.left(pos)
        if self.right(pos) is not None:
            yield self.right(pos)


    def siblings(self,pos):
        parent = self.parent(pos)
        if pos == self.left(parent):
            return self.right(parent)
        return self.left(parent)
    

