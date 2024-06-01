"""
This module provides an Class named 'ExpressionTree' that provides a few abstract methods and concrete methods for the implementation of
a Expression Tree ADT.

The code is purely based on my logic and might have some errors or bugs. 
Kindly feel free for any corrections or suggestions.

Author: Nithish Kumar S [3122 22 5002 084]

Created on: 28th June 2023

Revised on: 04th July  2023 
"""

from LinkedBinaryTree import LinkedBinaryTree


class ExpressionTree(LinkedBinaryTree):
    """
    This class is an implementation for a expression Tree ADT.

        It has the following methods:
            (i) A constructor to call the super constructor to initialize member data.
            (ii) A method 'consrtuct' to construct the tree and return root's address.
            (iii) A method 'inorder' for inorder traversal of the tree.
            (iv) A method '__str__' to print the tree itself.
            (v) A method 'mirror' to mirror the elements of the tree.
    """

    def __init__(self, item=None, Tleft=None, Tright=None):
        super().__init__(item, Tleft, Tright)

    # To construct the tree.
    def construct(self, str):
        s = []
        for ch in str:
            if ch in "+*/-":
                rchild = s.pop()
                lchild = s.pop()
                s.append(ExpressionTree(ch, lchild, rchild))
            else:
                s.append(ExpressionTree(ch))

        return s.pop()

    # for tree traversal.
    def inorder(self, pos):
        res = ""
        if pos is None:
            return None
        if pos.left is not None:
            res += self.inorder(pos.left)
        res += str(pos.item)
        if pos.right is not None:
            res += self.inorder(pos.right)
        return res

    # For printing the tree.
    def __str__(self):
        return str(self.inorder(self.root))

    # For mirroring elements of the tree.
    def mirror(self, pos=None):
        if pos is None:
            pos = self.root
        if pos.left is not None:
            self.mirror(pos.left)
        if pos.right is not None:
            self.mirror(pos.right)
        temp = pos.left
        pos.left = pos.right
        pos.right = temp


if __name__ == "__main__":
    # inputs to the construct functions are all postfix expressions.
    e1 = ExpressionTree()
    e1.root = e1.construct("ab*c/e-")
    print(e1.root)

    e2 = ExpressionTree()
    print(e2.construct("ab+a*cd-e+/afg-*h+-"))
