'''
This module provides a class 'Point' which helps to find the Euclidean distance between two points, which are created
as objects of the class. This exercise comes under the course UIT2201 (Programming and Data Structures).

This is a source code purely based on my logic. It may have some bugs as well. 

Kindly feel free to comment down your suggestions and/or opinions.

Created on: 19th April 2023

Revised on: 19th April 2023

Original Author: Nithish Kumar S
'''


class Vector:
    '''
    
    This version of class 'Vector' works for:
        -> the vector by itself passed as an argument (instead of the size of vector as an argument).
        
    This program module of class 'Vector' consists of:
    1. constructor __init__ to assign the vector argument to the obj instance,
    2. __len__  function overridden to return len of the vector argument (while len(obj) is asked),
    3. 'special functions / methods' to add, sub and mul the two vectors.
    
    '''
    
    #dimension stores the vector passed. For eg, if v1 = Vector([1,2,3]) ; v1.dimension = [1,2,3]
    
    dimension = 0

    def __init__(self,value):              #assigns dimension to the vector passed
        self.dimension =  value


    def __len__ (self):                    #len function is defined to return length of thee vector passed.   
        return len(self.dimension)


    def __eq__(self,other):                #checks if two vectors are of equal length / size.   
        return len(self) == len(other)
    
    
    def __add__(self,other):               #adds two vectors passed.
        if len(self) == len(other):
            result = [0] * len(self)
            for i in range(len(self)):
                result[i] = self.dimension[i] + other.dimension[i]
            return result
        else:
            return ValueError('Length of two vectors is not equal')
        
    
    def __sub__(self,other):               #subtracts two vectors passed.
        if len(self) == len(other):
            result = [0] * len(self)
            for i in range(len(self)):
                result[i] = self.dimension[i] - other.dimension[i]
            return result
        else:
            return ValueError('Length of two vectors is not equal')
        
    
    def __mul__(self,other):               #multiplies two vectors passed.
        if len(self) == len(other):
            result = 0

            for i in range(len(self)):
                result += self.dimension[i] * other.dimension[i]
            return result

        else:
            raise ValueError('Length of two vectors is not equal')
        
            
    def __str__(self):                     #using __str__ to return obj instance and not its memory location.              
        return str(self.dimension)



#usage of __name__ so that the test cases are not imported.

if __name__ == '__main__':
    
    v1 = Vector([1,2,3])

    v2 = Vector([4,5,6])

    print('The vector v1 is:',v1)
    print('\n The vector v2 is:',v2)


    print('\n --------------OUTPUTS-----------------')

    print("\n If v1 is equal to v2 in size:",v1==v2)                   #checking if vector are of equal sizes

    print("\n Addition result:",v1+v2)

    print("\n Subtraction result:",v1-v2)

    print("\n Multiplication result:",v1*v2)
