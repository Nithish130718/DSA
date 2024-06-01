'''
This module provides an Abstract Base Class named 'AbstractTree' that provides a few abstract methods and concrete methods for the implementation of
a Tree ADT.

The code is purely based on my logic and might have some errors or bugs. 
Kindly feel free for any corrections or suggestions.

Author: Nithish Kumar S [3122 22 5002 084]

Created on: 28th June 2023

Revised on: 28th June 2023 
'''

from abc import ABC,abstractmethod

class AbstractTree(ABC):
    '''
    This class is a Abstract Base class for a basic Tree ADT.
    It has the following methods:
        1) Abstract methods such as 'getroot','parent','num_children','children','__len__'.
        2) Concrete methods such as:
            (i) A method 'isroot' to check if a pos is the root node pos.
            (ii) A method 'isleaf' to check if a pos is the leaf node pos.
            (iii) A method 'isempty' to check if a Tree is empty.
            (iv) A method 'depthN' to check the depth of a tree.
            (v) A method 'heightN' to check the height of a node.
            (vi) A method 'height' to check the entire height of a tree.
    '''

    @abstractmethod
    def getroot(self):          
        pass


    @abstractmethod
    def parent(self,pos):
        pass
    

    @abstractmethod
    def children(self,pos):
        pass


    @abstractmethod
    def num_children(self):
        pass


    @abstractmethod
    def __len__(self):
        pass


    def isroot(self,pos):
        if pos == self.getroot():
            return True
        return False
    

    def isleaf(self,pos):
        if self.num_children(pos) == 0:
            return True
        return False
    

    def isempty(self):
        if self.getroot() == None or self.size == 0:
            return True
        return False
    

    # To find the depthN of a node.
    def depthN(self,pos):
        if self.isroot(pos):
            return 0
        else:
            return self.depthN(self.parent(pos))
        

    # For a node.
    def heightN(self,pos):
        if self.isleaf(pos):
            return 0
        else:
            temp = [self.heightN(child) for child in self.children(pos)]    # max height of children subtrees + 1 (pos)
            return (max(temp)+1)
        
    
    # For the tree itself.
    def height(self,pos=None):
        if pos is None: 
            if not self.isempty():
                pos = self.getroot()
                return self.height(pos)
            else:
                raise Exception('Tree is empty!')
            