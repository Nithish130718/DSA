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
        -> size of the vector passed as an argument (instead of the vector by itself as an argument).
        
    This program module of class 'Vector' consists of:
    1. constructor __init__ to create an empty list and to assign dimension (which describes vector size) to of size 'n' argument passed  
    2. __len__  function overridden to return len of the vector created (size passed as an argument already),
    3. __getitem__ and __set__item to take care of creating the vector list for given i/p and return as obj instance,
    4. 'special functions / methods' to add, sub and mul the two vectors.
    
    '''
    
    #coordinate = elements in of the vector list
    #dimension = size / len of the vector list
    dimension = 0

    def __init__(self,value):              #creates a list of length passed with all elements as 0.
        self.coordinate = [0] * value 
        self.dimension = value


    def __len__ (self):                    #sets length of the vector to dimension passed.   
        return self.dimension


    def __getitem__ (self,index):          #gets value for the vector list
        self.coordinate[index] = value


    def __setitem__ (self,index,value):    #sets value to the vector list
        self.coordinate[index] = value


    def __eq__ (self,other):               #checks if two vectors are equal
        if self.dimension == other.dimension:
            return True
        else:
            return False


    def __add__(self,other):              #adds two vectors
        if len(self) == len(other):
            result = [0] * len(self)

            for i in range(len(result)):
                result[i] = self.coordinate[i] + other.coordinate[i]
            return result

        else:
            raise ValueError


    def __sub__(self,other):              #subs two vectors
        if len(self) == len(other):
            result = [0] * len(self)

            for i in range(len(result)):
                result[i] = self.coordinate[i] - other.coordinate[i]
            return result

        else:
            raise ValueError


    def __mul__(self,other):              #muls two vectors and returns dot prod
        if len(self) == len(other):
            result = 0

            for i in range(len(self)):
                result += self.coordinate[i] * other.coordinate[i]
            return result

        else:
            raise ValueError

            
    def __str__(self):                     #using __str__ to return obj instance and not its memory location.              
        return str(self.coordinate)



#usage of __name__ so that the test cases are not imported.

if __name__ == '__main__':
    
    v1 = Vector(5)

    for i in range(len(v1)):
        value = int(input("Enter the element:"))
        v1[i] = value
    
    
    print("\n The vector v1 is:",v1,'\n')


    v2 = Vector(5)

    for i in range(len(v2)):
        value = int(input("Enter the element:"))
        v2[i] = value
    
    
    print("\n The vector v2 is:",v2)
    
    print('\n --------------OUTPUTS-----------------')

    print("\n If v1 is equal to v2:",v1==v2)                   #checking if vector are of equal sizes

    print("\n Addition result:",v1+v2)

    print("\n Subtraction result:",v1-v2)

    print("\n Multiplication result:",v1*v2)
