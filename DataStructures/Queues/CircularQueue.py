'''
This module provides a class 'CircularQueue' that provides implementation of a Circular Queue DS that potentially overcomes, the disadvantages
present in DynamicArrays.
'''

import ctypes

class Full_Queue(Exception):
    '''
    A class to raise the exception, if the Circular Queue surpasses the limit of m-1 elements (m-> capacity specified).
    '''
    pass


class CircularQueue:
    '''
    This class 'CircularQueue' is an implementation of the Circular Queue data structure.

    It has a constructor and the following functions/methods:
        -> Constructor assigns the member data required for the operations in the class.

        1) Method 'next' to increment rear and to bring it to 0, if it reaches the max capacity (cap-1).
        2) Function 'make_array' to make an empty Queue of the  specified  capacity.
        3) Functions 'isempty' and 'isfull' to check if the queue if empty or full.
        4) Method 'enqueue' to add elements onto the queue.
        5) Functions __getitem__ , 'len' and __str__ to get an element using index, to return len of the queue, and to print the queue respectively.

        REMARKS:
            The method of 'dequeue' is not implemented because, the quesion statement mentions 'orders cannot be deleted once placed'.
    '''

    def __init__(self,cap):
        # Constructor to assign the member data
        self.capacity = cap
        self.item = self.make_array(cap)
        self.rear = self.front = 0

    
    def next(self,pos):
        # Method to incremennt the rear. Main purpose is to bring the rear to 0 each time, it attains the max capacity (cap-1).
        return (pos+1) % self.capacity
    

    def make_array(self,cap):
        # Method to create an empty Queue using ctypes module for a specified capacity.
        temp = (cap * ctypes.py_object)()
        return temp
    

    def isempty(self):
        # Function to check if the Queue is empty.
        if self.front == self.rear:
            return True
        return False
    

    def isfull(self):
        # Function to check if the Queue is full.
        if (self.rear + 1) % self.capacity == self.front:
            return True
        else:
            return False


    def enqueue(self,ele):
        # Function to add the elements to a Queue at the rear position.
        if CircularQueue.isfull(self) == True:
            raise Full_Queue('Queue is full!')
        else:
            self.item[self.rear] = ele
            self.rear = self.next(self.rear)[]


    def __getitem__(self,index):
        # Method to get index using index.
        return self.item[index]
    

    def __len__(self):
        # Function to return the length of the Queue.
        return len(self.item)

    
    def __str__(self):
        # Function to return the Queue and its elements.
        string = '['
        count = 0
        for i in range(self.rear):
            if i == self.rear -1:
                string += str(self.item[i])
            else:
                string += str(self.item[i]) + ','
        string += ']'

        return string

       
if __name__ == '__main__':
    # Getting input for capacity and creating a Circular Queue of that capacity.
    m = int(input("Enter the maximum number of orders that can be placed:"))      #Getting input for max number of orders.
    cq = CircularQueue(m)

    # Assume cq is given as 3. So max nodes / cells that can be occupied is m-1 = 2.
    
    # Enqueuing elements to the Circular Queue and printing it afterwards.
    cq.enqueue(10)                     #Placing orders
    cq.enqueue(20)
    print(cq)
    
    # The circular queue has now reached the max number of elements. Any further attempts to enqueue elements into it will raise an exception.
    cq.enqueue(30)                     #No more orders can be placed.
    
    
