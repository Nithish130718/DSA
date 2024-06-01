"""
This module provides a class 'LinkedQueue' that provides an implementation to create and perform operations on a LinkedQueue.
This exercise comes under the course UIT2201 (Programming and Data Structures).

This is a source code purely based on my logic. It may have some bugs as well. 

Kindly feel free to comment down your suggestions and/or opinions.

Created on: 23st June 2023

Revised on: 30th June 2023

Original Author: Nithish Kumar S [IT-B, 3122 22 5002 084]
"""

from NodeCreation import Node


class LinkedQueue:
    """
    This class is an implementation of the LinkedQueue ADT.
    It consists of the following methods:
        1) A constructor '__init__' to initialize member data.
        2) A method 'isempty' to check if the LinkedQueue instance is empty.
        3) A method '__len__' that returns the length of the LinkedQueue instance.
        4) A method 'enqueue' to append elements to the LinkedQueue instance.
        5) A method 'find' to check if a search element is present in the LinkedQueue. If present, returns index-pos. Else, returns error message.
        6) Methods 'dequeue' to pop an element from the LinkedQueue intance.
        7) A method '__str__' to print the LinkedQueue instance itself.
    """

    # Constructor to initialize the member data - the 'head','front' and the 'rear' to the dummyheader and size = 0.
    def __init__(self):
        self.head = self.front = self.rear = Node()
        self.size = 0

    # Checks if a LinkedQueue object is empty.
    def isempty(self):
        if self.front == self.rear:
            return True
        return False

    # Returns length of the LinkedQueue object.
    def __len__(self):
        return self.size

    # Method to enqueue an element into the Queue.
    def enqueue(self, item):
        temp = Node(item)
        self.rear.next = temp
        self.rear = temp
        self.size += 1

    # To dequeue an element from the LinkedQueue instance.
    def dequeue(self):
        delnode = self.head.next
        self.front = delnode.next
        self.head.next = delnode.next
        self.size -= 1

    # Checks if a search element is in the LinkedQueue instance.
    def find(self, item):
        pos = self.head.next
        string, index = "", 0
        # If search item is the zero'th index, satisfies this if condition.
        if pos.item == item:
            string += f"Index: {index}, POS: {pos}"
            return string
        # Else, checks the index and pos of the item, if prresent in the LinkedQueue.
        while pos != None:
            if pos.item == item:
                string += f"Index: {index}, POS: {pos}"
                return string
            pos = pos.next
            index += 1
        # If item not in the LinkedQueue itself, returns an error message.
        return "The element you searched for is not in the LinkedQueue."

    # Method to print the LinkedQueue instance elements.
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

    # Creating an object instance of the LinkedQueue class.
    s = LinkedQueue()

    # Checking if empty (yes)
    print(f"Empty?: {s.isempty()}")

    # Appending data into the LinkedQueue.
    temp = [1, 2, 3, 4]
    for i in temp:
        s.enqueue(i)
    print("The LinkedQueue after appending operations is:", s)

    # Length finding
    print("\n The current length of the LinkedQueue instance is:", len(s))

    # dequeueping elements
    s.dequeue()
    print("\n The LinkedQueue after a dequeue operation is:", s)

    # Find operation
    print('\n Find operation for "3" result:', s.find(3))
    print('Find operation for "10" result:', s.find(10))
