'''

Question : 
    Implement a Stack class that maintains two stacks within a single array, with each stack growing from opposite ends of the array. 
    The implementation should include methods to check if the stack is full or empty, and a method to push elements into either of the two stacks. 
    Demonstrate how to create an instance of this Stack class with a specific capacity, and provide an example where elements are pushed into both stacks until the array is full, raising an exception if an attempt is made to push beyond the capacity.

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

    #Pushing 10 elements into the 2 Stacks as per index 0 or 1 respectively. here, 0 means stack1, 1 means stack2
    # Cap of each stack = 10/2. 
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
