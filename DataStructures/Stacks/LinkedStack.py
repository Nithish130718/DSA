"""
This module provides a class 'LinkedStack' that provides an implementation to create and perform operations on a LinkedStack.
This exercise comes under the course UIT2201 (Programming and Data Structures).

This is a source code purely based on my logic. It may have some bugs as well. 

Kindly feel free to comment down your suggestions and/or opinions.

Created on: 23st June 2023

Revised on: 30th June 2023

Original Author: Nithish Kumar S [IT-B, 3122 22 5002 084]
"""

from NodeCreation import Node


class LinkedStack:
    """
    This class is an implementation of the LinkedStack ADT.
    It consists of the following methods:
        1) A constructor '__init__' to initialize member data.
        2) A method 'isempty' to check if the LinkedStack instance is empty.
        3) A method '__len__' that returns the length of the LinkedStack instance.
        4) A method 'push' to append elements to the LinkedStack instance.
        5) A method 'find' to check if a search element is present in the LinkedStack. If present, returns index-pos. Else, returns error message.
        6) Methods 'pop' to pop an element from the LinkedStack intance.
        7) A method '__str__' to print the LinkedStack instance itself.
    """

    # Constructor to initialize the member data - the 'head' and the 'top' to the dummyheader and size = 0.
    def __init__(self):
        self.head = self.top = Node()
        self.size = 0

    # Checks if a LinkedStack object is empty.
    def isempty(self):
        if self.head == self.top:
            return True
        return False

    # Returns length of the LinkedStack object.
    def __len__(self):
        return self.size

    # Method to push an element into the stack.
    def push(self, item):
        temp = Node(item)
        self.top.next = temp
        self.top = temp
        self.size += 1

    # To pop an element from the LinkedStack instance.
    def pop(self):
        pos = self.head.next
        for i in range(self.size - 2):
            pos = pos.next
        self.top = pos
        self.top.next = None
        self.size -= 1

    # Checks if a search element is in the LinkedStack instance.
    def find(self, item):
        pos = self.head.next
        string, index = "", 0
        # If search item is the zero'th index, satisfies this if condition.
        if pos.item == item:
            string += f"Index: {index}, POS: {pos}"
            return string
        # Else, checks the index and pos of the item, if prresent in the LinkedStack.
        while pos != None:
            if pos.item == item:
                string += f"Index: {index}, POS: {pos}"
                return string
            pos = pos.next
            index += 1
        # If item not in the LinkedStack itself, returns an error message.
        return "The element you searched for is not in the LinkedStack."

    # Method to print the LinkedStack instance elements.
    def __str__(self):
        result = "["
        pos = self.head.next
        while pos != None:
            if pos.next is not None:
                result += str(pos.item) + ","
            else:
                result += str(pos.item)
            pos = pos.next
        result += "]"
        return result


# Usage of __name__ so that the test cases are not imported.

if __name__ == "__main__":

    # Creating an object instance of the LinkedStack class.
    s = LinkedStack()

    # Checking if empty (yes)
    print("Empty?:", s.isempty(), "\n")

    # Appending data into the LinkedStack.
    temp = [1, 2, 3, 4]
    for i in temp:
        s.push(i)
    print("The LinkedStack after appending operations is:", s)

    # Length finding
    print("\n The current length of the LinkedStack instance is:", len(s))

    # Popping elements
    s.pop()
    print("\n The LinkedStack after a pop operation is:", s)

    # Find operation
    print('\n Find operation for "1" result:', s.find(1))
    print('Find operation for "10" result:', s.find(10))
