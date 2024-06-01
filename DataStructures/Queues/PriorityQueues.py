'''
This module provides a class 'Queue' that prrovides implementation to maintain two queues as:
    -> High Priority Queue(HPQ)
    -> Low Priority Queue(LPQ)
This exercise comes under the course UIT2201 (Programming and Data Structures).

This is a source code purely based on my logic. It may have some bugs as well. 

Kindly feel free to comment down your suggestions and/or opinions.

Created on: 06th June 2023

Revised on: 06th June 2023

Original Author: Nithish Kumar S [IT-B, 3122 22 5002 084]
'''

import ctypes

class Queue:
    '''
    This class 'Queue' contains a constructor and 4 methods as follows:
         -> A constructor __init__ that assigns the member data.

         1) Function  'isempty' to check if the Queue is empty.
         2) Function __getitem__ to get the element using its index.
         3) Functions 'enqueue' and 'dequeue' to add or remove elements from the queues.     
    '''

    def __init__(self):
        # Constructor to assign the member data
        self.hpq = []                             # High Priority Queue(HPQ)
        self.lpq = []                             # Low Priority Queue(LPQ)
        #The front and rear of both HPQ and LPQ set to 0 initially.
        self.hpq_f = self.hpq_r = 0
        self.lpq_f = self.lpq_r = 0


    def isempty(self):
        # Function to check if the Queue is empty.
        return len(self) == 0
    
    
    def __getitem__(self,index):
        # Function to get elements from the Queue using their indices.
        return self[index]
    
    
    def enqueue(self,index,ele):
        # Method to enqueue(add) elements into the HPQ or LPQ as per the choice (indicated by the 'index' argument).
        if index == 0: 
            self.hpq.append(ele)
            self.hpq_r += 1
        elif index == 1:
            self.lpq.append(ele)
            self.lpq_r += 1
        

    def dequeue(self):
        # Method to dequeue(remove) elements as:
        #   -> Dequeue happens at the HPQ initially until its empty.
        #   -> Once HPQ is empty, dequeue occurs at the LPQ.
        if Queue.isempty(self.hpq) != True:
            self.hpq.pop(0)
        else:
            self.lpq.pop(0)
            self.lpq_f += 1


    def __str__(self):
        # Method to print the Queue itself.
        return '[' + str(self) + ']'



#----------------------------------------------------------------DRIVER CODE----------------------------------------------------------------

if __name__ == '__main__':
    #Creating an object instance of the Queue class.
    p = Queue()

    #Adding 3 elements to HPQ and LPQ using 'enqueue' method.
    print('Creating an object instance and enqueuing elements to the HPQ and LPQ using index 0 or 1.')
    p.enqueue(0,10)
    p.enqueue(0,20)
    p.enqueue(0,30)
    p.enqueue(1,40)
    p.enqueue(1,50)
    p.enqueue(1,60)
    print('High priority Queue:',p.hpq)
    print('Low priority Queue:',p.lpq)

    #Dequeuing elements removes elements from the HPQ initally.
    print('\n Dequeuing elements - happens at HPQ until its empty. Here, dequeuing 3 elements now -> HPQ becomes empty.')
    p.dequeue()
    p.dequeue()
    p.dequeue()
    print('High priority Queue:',p.hpq)
    print('Low priority Queue:',p.lpq)
    
    #Once HPQ is empty, dequeue removes elements from the LPQ.
    print('\n Now HPQ is empty and dequeuing occurs at the LPQ.')
    p.dequeue()
    print('High priority Queue:',p.hpq)
    print('Low priority Queue:',p.lpq)
        


