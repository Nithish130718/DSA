"""
This module provides an Class named 'LinkedBinaryTree' that provides a few abstract methods and concrete methods for the implementation of
a LLinked Binary Tree ADT.

The code is purely based on my logic and might have some errors or bugs. 
Kindly feel free for any corrections or suggestions.

Author: Nithish Kumar S [3122 22 5002 084]

Created on: 28th June 2023

Revised on: 04th July 2023 
"""

from AbstractBinaryTree import AbstractBinaryTree


class LinkedBinaryTree(AbstractBinaryTree):
    """
        This class is an implementation of the LinkedBinaryTree ADT.

        It consists of a subclass named 'BTNode' that facilitates the creation of a Node and assigning its member data such as item,left,right,parent.
    In addition, it has a __getitem__ and __setitem__ to get data from an index and to set item to an index.

        It consists of the following methods:
            1) A constructor '__init__' to initialize member data and to add a subtree to an existing tree.
            2) A method 'addRoot' to add an element as the root.
            3) Methods 'addLeft' and 'addRight' to add elements as left or right child of a specified pos of a LinkedBinaryTree instance.
            4) A method 'getroot' to get the root item of the LinkedBinaryTree instance.
            5) A method 'parent' to find the parent element of a node.
            6) A method 'num_children' to get the number of children of a node of a LinkedBinaryTree instance.
            7) A method '__len__' to return the length (total size) of a LinkedBinaryTree instance.
            8) Methods 'left' and 'right' to return the left and right item of a LinkedBinaryTree instance.
            9) A method for a 'preorder' traversal of the LinkedBinaryTree instance.
            10) A method '__str__' to print the LinkedBinaryTree instance itself using preoder traversal.
            11) A method 'find_leaf_nodes' that will find the leaf nodes of a LinkedBinaryTree instance.
    """

    # Just an alternate way to store items in a list and access it directly.
    global elements
    elements = []

    class BTNode:

        __slots__ = ["item", "left", "right", "parent"]

        def __init__(self, item, left=None, right=None, parent=None):
            self.item = item
            self.left = left
            self.right = right
            self.parent = parent
            elements.append(item)

        # To get the item of a specified index.
        def __getitem__(self):
            return self.item

        # To set item to a specified index.
        def __setitem__(self, item):
            self.item = item

    __slots__ = ["size"]

    def __init__(self, item=None, Tleft=None, Tright=None, parent=None):
        self.root = None
        self.size = 0

        if item is not None:
            self.root = self.addRoot(item)

        # Adding a subtree to as left child
        if Tleft is not None:
            if Tleft.root is not None:
                Tleft.root.parent = self.root
                self.root.left = Tleft.root
                self.size += Tleft.size
                Tleft.root, Tleft.size = None, 0

        # Adding a subtree to as right child
        if Tright is not None:
            if Tright.root is not None:
                Tright.root.parent = self.root
                self.root.right = Tright.root
                self.size += Tright.size
                Tright.root, Tright.size = None, 0

    # Method to add an item as the root Node.
    def addRoot(self, item):
        if self.root is not None:
            raise ValueError("Root already exists!")
        temp = self.BTNode(item)
        self.root = temp
        self.size += 1
        return self.root

    # Method to add an element as left child of a pos.
    def addLeft(self, item, pos):
        if self.left(pos) is not None:
            raise ValueError("A left child already exists!")
        pos.left = self.BTNode(item, parent=pos)
        self.size += 1
        return pos.left

    # Method to add an element as right child of a pos.
    def addRight(self, item, pos):
        if self.right(pos) is not None:
            raise ValueError("A right child already exists!")
        pos.right = self.BTNode(item, parent=pos)
        self.size += 1
        return pos.right

    # Method to get the root of a tree.
    def getroot(self):
        return self.root

    # To get the parent node of a specified node.
    def parent(self, pos=None):
        if pos is not None:
            return pos.parent
        return self.root

    # To get no of children of a node.
    def num_children(self, pos=None):
        if pos is None:
            pos = self.root
        children_count = 0
        if pos.left is not None:
            children_count += 1
        if pos.right is not None:
            children_count += 1
        return children_count

    def __len__(self):
        return self.size

    # Method to get the left child of a node
    def left(self, pos):
        return pos.left

    # Method to get the right child of a node
    def right(self, pos):
        return pos.right

    # To facilitate preorder traversal.
    def preorder(self, pos=None):
        if pos is None:
            pos = self.root
        result = str(pos.item)
        if pos.left is not None:
            result += " " + self.preorder(pos.left) + " "
        if pos.right is not None:
            result += " " + self.preorder(pos.right) + " "

        return result

    # str method to print the tree itself.
    def __str__(self):
        if not self.isempty():
            string = self.preorder()
            return string
        return "Tree does not exist my child!"

    # Method to find the leaf nodes of a tree.
    def find_leaf_nodes(self):
        leaf_nodes = []

        if self.isempty():
            return None

        stack = [self.getroot()]

        while stack:
            node = stack.pop()

            if node.left is None and node.right is None:
                leaf_nodes.append(node.item)

            if node.right is not None:
                stack.append(node.right)

            if node.left is not None:
                stack.append(node.left)

        return leaf_nodes


if __name__ == "__main__":
    # Creating a tree -> adding a root -> adding left and right children.
    t = LinkedBinaryTree()
    t.addRoot(10)
    t.addLeft(20, t.root)
    t.addRight(30, t.root)
    print(t)

    # Creating a tree with only one element (root)
    t1 = LinkedBinaryTree(40)

    # Creating a new tree with previous trees as left and right children respectively.
    t2 = LinkedBinaryTree(0, t, t1)
    print(t2)

    # Printing root node address and checking if empty.
    print("Root Node:", t2.getroot())
    print("Is t2 empty?:", t2.isempty())

    # Checking if leaf or root
    print("Is root?:", t2.isroot(t2.root))  # Root is root => True.
    print(
        "Is leaf?:", t2.isleaf(t2.root)
    )  # Root is not leaf node here => False. True for t1.isleaf(t1.root)

    # To get total no. of nodes in a tree.
    print(t2.size)
    print(len(t2))

    # Checking depth and height functions.
    print(t2.depthN(t2.root))  # Depth of root node is 0.
    print(t2.heightN(t2.root))  # Height of tree = 2.

    # Other functions.
    print(t2.children(t2.root))  # returns address of children.
    print(t2.num_children())  # for root node => no of child - 2.

    # Finding leaf nodes of a tree.
    print(t2.find_leaf_nodes())


"""
    
    print(elements)                       # alternate way to print the elements
"""
