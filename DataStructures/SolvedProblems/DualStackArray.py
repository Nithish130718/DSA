'''
This module provides a class 'Stack' that enables to maintain 2 stacks in a single array (at the two ends of the array).
This exercise comes under the course UIT2201 (Programming and Data Structures).

This is a source code purely based on my logic. It may have some bugs as well. 

Kindly feel free to comment down your suggestions and/or opinions.

Created on: 31st May 2023

Revised on: 03rd June 2023

Original Author: Nithish Kumar S [IT-B, 3122 22 5002 084]
'''


import ctypes

class FullStack(Exception):
    pass

class Stack:
    def __init__(self,val):
        self.capacity =  val
        self.top1 = 0
        self.top2 = val - 1
        self.A = self.make_array(val)

    def make_array(self,cap):
        temp = (cap * ctypes.py_object)()
        return temp
    
    def isfull(self):
        if self.top1 > self.top2 or self.top2 < self.top1:
            return True
        
    def isempty(self):
        if self.top1 == 0 and self.top2 == self.capacity:
            return True
        
    def __getitem__(self,index):
        return self.A[index]
    
    def push(self,index,ele):
        if Stack.isfull(self) == True:
            raise FullStack('Array is full')
        if index == 0:
            self.A[self.top1] = ele
            self.top1 += 1
        elif index == 1:
            self.A[self.top2] = ele
            self.top2 -= 1
        else:
            raise IndexError('Wrong index')


        

if __name__ == '__main__': 
    #Creating an object instance of capacity 10.      
    s = Stack(10)

    #Pushing 10 elements into the 2 Stacks as per index 0 or 1 respectively. Cap of each stack = 10/2. 
    #Pushing continues smoothly until the the number of elements doesn't surpass the capacity.
    s.push(0,1)
    s.push(1,2)
    s.push(0,3)
    s.push(1,4)
    s.push(0,5)
    s.push(1,6)
    s.push(0,7)
    s.push(1,8)
    s.push(0,9)
    s.push(1,10)
    
    #Now the array containing 2 stacks is full! Pushing any more elements will raise an exception.
    s.push(0,11)
