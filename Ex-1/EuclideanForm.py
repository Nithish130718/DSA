# -*- coding: utf-8 -*-
'''
This module provides a function finds the P-norm form or the Euclidean form of a vector (given as a sequence of elements)
based on thee power of the sequence. This exercise comes under the course UIT2201 (Programming and Data Structures).

This is a source code purely based on my logic. It may have some bugs as well. 

Kindly feel free to comment down your suggestions and/or opinions.

Created on: 12th April 2023

Revised on: 12th April 2023

Original Author: Nithish Kumar S 
'''


import random

def norm(v,p=2):
    '''
    Parameters: v - The sequence of elements (of the vector) and,
                p - The power. By default, p = 2, which denotes the Euclidean form.
    ----------
    
    This 'norm' function finds the p-norm or Euclidean norm of a vector (given as a sequence of elements) and a 
    ceratin power,p.

    Returns: Euclidean form or p-norm form based on power,
             Zero, if the vector sequence is empty.
    '''
    
    
    if len(v)>0:
        p_norm = 0
        
        for i in range(len(v)):
            p_norm += v[i] ** p
        
        if p!=2:
            print("The power is:",p)
            print("The p-norm value is:",p_norm ** (1/p))
            
        else:
            print("The Euclidean form value is:",p_norm ** 0.5)
        
    elif p!=2:
        print("The power is:",p)
        print("The p-norm value is 0.")
        
    else:
        print("The Euclidean value is 0.")
        
    

def tuple_creation(size=5,low=0,high=10):
    '''
    This function creates tuple  of integers for the given input sizes.
    size: size of the tuple (length).
    low: lowest value that can be present in the tuple.
    high: highest value that can be present in the tuple.
    
    Returns: created tuple for the given input size and defined range, if input is given.
             a tuple created with the default arguments, if no arguments are passed.
    '''
    
    v = ()
    
    for i in range(size):
        element = random.randint(low,high)
        v+= (element,)
    
    return v


#using __name__ so that the test cases are not imported.
if __name__ == '__main__':
    
    '''
    norm(v,power) = P-norm value
    norm(v) = Euclidean form value
    '''
    
    #test case 1 with random power between 3-9 and positive integer elements
    v=tuple_creation(4,3,7)
    print("The vector's sequence of elements is:",v)
    norm(v,random.randint(3,9))
    norm(v)
    
    print()
    
    #test case 2 with random power between 3-9 and negative integer elements
    v=tuple_creation(5,-5,-1)
    print("The vector's sequence of elements is:",v)
    norm(v,random.randint(3,9))
    norm(v)
    
    print()
    
    #test case 3 with a negative power between -3 and -9 and positive integer elements
    v=tuple_creation(4,3,7)
    print("The vector's sequence of elements is:",v)
    norm(v,random.randint(-9,-3))
    norm(v)
    
    print()
    
    #test case 4 with a negative power between -3 and -9 and negative integer elements
    v=tuple_creation(5,-5,-1)
    print("The vector's sequence of elements is:",v)
    norm(v,random.randint(-9,-3))
    norm(v)
    
    print()
    
    #test case 5 with an empty tuple
    v=()
    print("The vector's sequence of elements is:",v)
    norm(v,random.randint(-9,9))
    norm(v)
    
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
