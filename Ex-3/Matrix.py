'''
This module provides a class 'Matrices' which helps to perform addition, subtraction and multiplication
of two matrices. This exercise comes under the course UIT2201 (Programming and Data Structures).

This is a source code purely based on my logic. It may have some bugs as well. 

Kindly feel free to comment down your suggestions and/or opinions.

Created on: 19th April 2023

Revised on: 28th April 2023

Original Author: Nithish Kumar S 
'''


import random

class Matrix:
    
    '''
    
    This class 'Matrix' works for:
        -> rows and columns of a matrix passed as an argument (instead of the matrix by itself as an argument).
        
    This program module of class 'Matrix' consists of:
    1. constructor __init__ to create an empty atrix to which the elements will be assigned to, next.
    2. __str__ function to return or print th result as required.
    2. __len__  function overridden to return len of the matrix as number of rows in it.
    3. __set__item to take care of assiging values to the matrix (values created using random),
    4. 'special functions / methods' to add, sub and mul the two matrices.
    
    '''
    
    rows = 0
    columns = 0
    
    #Constructor defined to create an empty matrix to which the elements will be assigned to, next.
    def __init__ (self,r,c):
        self.rows = r
        self.columns = c
        self.matrix = []

        for i in range(r):
            row_ele = [0]*c
            self.matrix.append(row_ele)


    #To return or print the result
    def __str__(self):
        display = ''
        for i in range(self.rows):
            if i == self.rows - 1:
                display += str(self.matrix[i])
            else:
                display += str(self.matrix[i]) + '\n'

        return '[' + display + ']'


    # len function overridden to return length of the matrix as self.rows (number of rows  == length)
    def __len__(self):
        return self.rows
    
    
    #Fuuc to set or assign values to each element in the matrix like a11,a22,.....etc,.
    def __setitem__ (self,index,value):
        self.matrix[index[0]][index[1]] = value
        
    
    #Func to add the two given matrices
    def __add__  (self,other):
        if self.rows == other.rows and self.columns == other.columns:
            result = []
            for i in range(len(self.matrix)):
                result.append([])
                for j in range(len(self.matrix[0])):
                    result[i].append(self.matrix[i][j] + other.matrix[i][j])
            
            for i in result:
                print(i)
                
        else:
            raise ValueError('Addition cannot be performed for these two matrices')
        
    
    
    #Func to subtract the two given matrices
    def __sub__  (self,other):
        if self.rows == other.rows and self.columns == other.columns:
            result = []
            for i in range(len(self.matrix)):
                result.append([])
                for j in range(len(self.matrix[0])):
                    result[i].append(self.matrix[i][j] - other.matrix[i][j])
            
            for i in result:
                print(i)
                
        else:
            raise ValueError('Subtraction cannot be performed for these two matrices')
    
    
    #Func to multiply the two given matrices
    def __mul__  (self,other):
        if self.columns != other.rows:
            raise ValueError('Cannot perform multiplcation for these matrices!')
        else:
            result = [[0 for j in range(other.columns)] for i in range(self.rows)]
            for i in range(self.rows):
                for j in range(other.columns):
                    for k in range(other.rows):
                        result[i][j] += self.matrix[i][k] + other.matrix[k][j]
            
            for i in result:
                print(i)
                    
    
  
#Usage of __name__ so that the test cases are not imported.
         
if __name__ == '__main__':
    
    m1 = Matrix(3,3)

    for i in range(len(m1)):
        for j in range(len(m1)):
            element = random.randint(-5,5)
            m1[(i,j)] = element    
    print('The matrix one is: \n',m1)


    m2 = Matrix(3,3)

    for i in range(len(m1)):
        for j in range(len(m1)):
            element = random.randint(-5,5)
            m2[(i,j)] = element
    print('\n The m2 matrix is: \n',m2)


    print('\n Addition result:')                       #Addition of two matrices 
    m1+m2


    print('\n Subtraction result:')                    #Subtraction of two matrices
    m1-m2


    print('\n Multiplication result:')                 #Multiplication of two matrices
    m1*m2












