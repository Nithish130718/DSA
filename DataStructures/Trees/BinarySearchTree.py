"""
This module provides an Abstract Base Class named 'AbstractBinaryTree' that provides a few abstract methods and concrete methods for the implementation of
a Tree ADT.

The code is purely based on my logic and might have some errors or bugs. 
Kindly feel free for any corrections or suggestions.

Author: Nithish Kumar S [3122 22 5002 084]

Created on: 28th June 2023

Revised on: 28th June 2023 
"""

from LinkedBinaryTree import LinkedBinaryTree


class BinarySearchTree(LinkedBinaryTree):
    """
    This class is a class implementation of BinarySearchTree.
    It has the following methods:
        1) A constructor to initialize data.
        2) Methods such as:
            (i) A method 'insert' to insert elements items into the BST.
            (ii) A method 'search' to search for an item pos in the BST.
            (iii) Methods 'findmin' and 'findmax' to find the minimum and maximum values in a BST.
            (iv) A method 'parent' to return the parent pos of a node.
            (v) A method 'delete' to delete a node specifiying item value.
            (vi) A __str__ method to print the BST supported by the method of "inorder" traversal.
    """

    def __init__(self, item=None, Tleft=None, Tright=None):
        super().__init__(item, Tleft, Tright)

    def insert(self, item, pos):
        if item == pos.item:
            return
        elif item < pos.item:
            if pos.left is None:
                pos.left = self.addLeft(item, pos)
            else:
                self.insert(item, pos.left)
        elif item > pos.item:
            if pos.right is None:
                pos.right = self.addRight(item, pos)
            else:
                self.insert(item, pos.right)

    def search(self, item, pos):
        if item == pos.item:  # if item equals root item.
            return pos
        elif item < pos.item and pos.left is not None:  # smaller than root
            return self.search(item, pos.left)
        elif item > pos.item and pos.right is not None:  # greater than root
            return self.search(item, pos.right)

    def Find_min(self, pos=None):
        if pos is None:
            return pos.parent
        elif pos.left is not None:
            return self.Find_min(pos.left)
        else:
            return pos

    def Find_max(self, pos=None):
        if pos is None:
            return pos.parent
        elif pos.right is not None:
            return self.Find_max(pos.right)
        else:
            return pos

    def parent(self, pos):
        return pos.parent

    def delete(self, item):
        pos = self.search(item, self.root)
        if pos is None:
            print("Item not in tree")
            return

        parent = pos.parent

        if pos.left is None and pos.right is None:  # no children
            if parent.left == pos:
                parent.left = None
                self.size -= 1
                return
            elif parent.right == pos:
                parent.right = None
                self.size -= 1
                return

        elif (
            pos.left is not None and pos.right is None
        ):  # 1 child and it is the left child
            parent.left = pos.left
            pos.parent = pos.left = pos.right = None
            self.size -= 1

        elif (
            pos.right is not None and pos.left is None
        ):  # 1 child and it is the right child
            parent.right = pos.right
            pos.parent = pos.left = pos.right = None
            self.size -= 1

        else:  # 2 children
            r = self.Find_min(pos.right)
            pos.item = r.item
            r.item = 100000
            self.delete(r.item)

    # For an inorder traversal.
    def Inorder(self, pos, res):
        if pos.left is not None:
            res = self.Inorder(pos.left, res)
        res += str(pos.item) + " "
        if pos.right is not None:
            res = self.Inorder(pos.right, res)
        return res

    # To print the tree itself.
    def __str__(self):
        if not self.isempty():
            return str(self.Inorder(self.root, res=""))
        else:
            return None

    # Level order traversal
    def LevelOrder(self,root):
        h = self.height(root)
        for i in range(1, h+1):
            self.printCurrentLevel(root, i)     # starts from root. then goes recursive

    # helper function in LO traversal.
    def printCurrentLevel(self,root, level):
        if root is None:            # empty tree
            return
        if level == 1:              # prints current level
            print(root.item, end=" ")
        elif level > 1:             # for all nodes which has level > 1 (has child nodes)
            self.printCurrentLevel(root.left, level-1)
            self.printCurrentLevel(root.right, level-1)

    # gets max height of the subtrees to get height of the tree
    def height(self,node):
        if node is None:
            return 0
        else:
            lheight = self.height(node.left)
            rheight = self.height(node.right)
            if lheight > rheight:       # return max height condition
                return lheight+1
            else:
                return rheight+1

if __name__ == "__main__":
    # Creating an instance.
    bst = BinarySearchTree(
        10
    )  # adding 10 as root and inserting the elemenets into the tree.
    bst.insert(20, bst.root)
    bst.insert(30, bst.root)
    bst.insert(35, bst.root)
    bst.insert(40, bst.root)
    bst.insert(73, bst.root)
    bst.insert(23, bst.root)
    print(f"\n {bst} \n")

    x = bst.search(10, bst.root)  # search operation
    if x is None:
        print("Item not in tree")
    else:
        print(f"Item found. pos : {x} \n")

    x = bst.Find_max(bst.root)  # finding maximum val.
    print(f" Max item: {x.item} \n ")

    x = bst.Find_min(bst.root)  # finding minimum val.
    print(f"Min item: {x.item} \n")

    print(
        f"Number of nodes (BST Size) : {bst.size} \n"
    )  # Printing number of nodes in the bst

    bst.delete(20)  # deleting an item.
    print(f" BST after deletion: {bst}")

    # level order traversal
    print(bst.LevelOrder(bst.root))
