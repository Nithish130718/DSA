'''
This module provides a class 'DynamicArrays' which helps for the implementation of list ADT.
This exercise comes under the course UIT2201 (Programming and Data Structures).

This is a source code purely based on my logic. It may have some bugs as well. 

Kindly feel free to comment down your suggestions and/or opinions.

Created on: 12th April 2023

Revised on: 13th April 2023

Original Author: Nithish Kumar S 
'''


import ctypes
import random
import time

class DynamicArrays:

    '''
    This class is designed for the implementation of the List ADT in python. 

    The class contains the following functions:
    1) A constructor __init__
    2) Two functions 'make_array' and 'resize' to make an empty array and resizing it, if needed.
    3) A function __len__ to find out the length of the array
    4) The functions '__getitem__' and '__setitem__' to get an element from an index i/p and to set an element at a specified index.
    5) The functions 'append','insert','delete','extend','__contains__','index','count' to perform the related operations.
    6) A '__str__' function to print the array elements.

    '''

    #Constructor
    def __init__(self,val):
        if isinstance(val,int):               #Passing a capacity as an argument
            self.n=0
            self.cap=val
            self.A=self.make_array(self.cap)
        else:                                 #If a array is passed as argument
            self.n=len(val)-1
            self.cap=len(val)
            self.A=val


    def make_array(self,cap):
        '''
        The function 'make_array' creates an empty array for a specified capacity for future assignment or storage of data.
        '''

        if cap==0:                                            #creates an array of cap 1, if cap = 0 was given.
            temp=((int(cap)+1)*ctypes.py_object)()
            self.cap=1
        else:                                                 #creates an array of specified cap.
            temp=(cap*ctypes.py_object)()
        return temp


    def resize(self,cap):
        '''
        The function 'resize' basically resizes the array, in the sense, it modifies (expands/shrinks) the array.
        '''

        B=self.make_array(cap)
        for i in range(self.n):
            B[i]=self.A[i]             #shifting data from A to B
        self.A=B                       #changing memory reference of temp array B to initial array A.

    
    def __len__(self):
        '''
        Overriding the inbuilt '__len__' function for our user defined class.
        '''
        return self.n
    

    def __getitem__(self,index):
        '''
        This function basically returns you the element present at a specified index.
        '''

        if index>self.n or index<0:
            raise IndexError("Index out of range")
        else:
            return self.A[index]


    def __setitem__(self,index,element):
        '''
        This special method sets the element to the
        particular index. Both are taken in as inputs from
        the user.
        '''

        if index>self.n or index<0:
            raise IndexError("Index out of range")
        else:
            self.A[index]=element


    def append(self,element):
        '''
        The function 'append' is an overrided method of the inbuilt 'append' function. It adds elements to end of the array. If n == cap, resizes array.
        '''

        if self.n==self.cap:
            self.cap=self.cap*2
            self.resize(self.cap)
        self.A[self.n]=element
        self.n+=1
        

    def insert(self,index,element):
        '''
        This method inserts the element into a desired index
        given as inputs..
        '''

        if not(0<=index<=self.n):
            raise IndexError("Index out of range")
        else:
            if self.n==self.cap:
                self.cap*=2
                self.resize(self.cap)
            for i in range(self.n,index,-1):
                self.A[i]=self.A[i-1]
            self.A[index]=element
            self.n+=1
    

    def delete(self,index):
        '''
        This method deletes the element in the index
        specified by the user as an input.
        '''

        if not(0<=index<=self.n):
            raise IndexError("Index out of range")
        else:
            for i in range(index,self.n-1):
                self.A[i]=self.A[i+1]
            self.n-=1
            if (self.cap//4)>self.n:
                self.cap=self.cap//2
                self.resize(self.cap)
    
    def extend(self,other):
        '''
        This method extends one list ADT with another
        list ADT which given as input.
        '''

        self.resize((self.cap+other.cap)*2)
        for i in range(other.n):
            self.A[self.n+i]=other.A[i]
        self.n+=other.n
            

    def __contains__(self,element):
        '''
        This special method checks if the element is in the 
        array. Returns true if it is present else returns false.
        '''

        for index in range(0,self.n):
            if self.A[index]==element:
                return True
        return False
        
    
    def index(self,element):
        '''
        This method returns the index of the first 
        occurrence of the element in the array.
        '''

        for index in range(0,self.n):
            if self.A[index]==element:
                return index
        raise ValueError("Element is not present in the list.")
    

    def count(self,element):
        '''
        This method counts the total number of occurrences
        in the array and returns the count of it.
        '''

        count=0
        for index in range(0,self.n):
            if self.A[index]==element:
                count+=1
        return count


    def __str__(self):
        '''
        This special method prints the array in the format of
        a built-in list but in string type after type casting.
        '''

        values=""
        for i in range(self.n):
            if i==int(self.n)-1:
                values+=str(self.A[i])
            else:
                values+=str(self.A[i])+", "
        return "["+values+"]"
    


#Driver code
if __name__=="__main__":

    start = time.time()

    #Creating a listADT object
    p= DynamicArrays(5)

    #Adding an element to the empty list object
    p.append(1)
    print(p)

    #Adding n elements to the object
    total = 0
    n = int(input("Enter number of elements you wish to append:"))
    for i in range(n):
        start = time.time()
        p.append(random.randint(-10,10))
        end = time.time()
        total +=  end - start
    print(p)
    print('Time taken for execution for n appends is:',total)       #time taken for n appends 
    
    #Extending the list object with another list ADT object
    p2=DynamicArrays(4)
    p2.append(1)
    p2.append(2)
    p2.append(3)
    p2.append(4)
    p.extend(p2)
    print('The array after extend is:',p)

    #Length of the list object
    print('Length of the array is:',len(p))

    #To find the index of 3
    print('Index of 3 is:',p.index(3))

    #Removing the element in 3rd index
    p.delete(3)
    print('Array after deleting 3rd index element:',p)

    #inserting 7 at 4th index
    p.insert(4,7)
    print('Array after inserting 4 at 7th index is:',p)

    #Checking if the list object contains 7
    print('If 7 is in the array?:',7 in p)

    #Counting the total number of occurrences of 1 in the list object
    print('The total number of occurrences of 1 in the array is:',p.count(1))

    #Setting the value of the 0th index as 5
    p[0]=5
    print(p)

    #Printing the element at 2nd index
    print(p[2])

    
