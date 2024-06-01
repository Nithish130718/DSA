# -*- coding: utf-8 -*-
'''
This module provides 3 functions (one called inside the other) that checks if the input integer values can satisfy 
the given arithmetic formulas (or its variations).This exercise comes under the course UIT2201 (Programming and 
Data Structures).

This is a source code purely based on my logic. It may have some bugs as well. 

Kindly feel free to comment down your suggestions and/or opinions.

Created on: 8th April 2023

Revised on: 9th April 2023

Original Author: Nithish Kumar S 
'''


def formula_1(a,b,c):
    '''
    Parameters: a,b,c being three input numbers.
    ----------
    
    This function checks if the input integers satisfy the addition formula a+b=c or its variations.
    
    Returns: if condition == True, prints 'satisfies equation',
             else, prints nothing.
    '''
    
    condition = False
    if a+b == c:
        condition = True
    elif a+c == b:
        condition = True
    elif b+c == a:
        condition = True
    
    if condition == True:
        print("The given values satisfies 'a+b=c' or one of its variations.")
        
    formula_2(a,b,c)
    
    
def formula_2(a,b,c):
    '''
    Parameters: a,b,c being three input numbers.
    ----------
    
    This function checks if the input integers satisfy the subtraction formula a=b-c or its variations.
    
    Returns: if condition == True, prints 'satisfies equation',
             else, prints nothing.
    '''
    condition = False
    if a == b-c or a == c-b:
        condition = True
    elif b == a-c or b == c-a:
        condition = True
    elif c == a-b or c == b-a:
        condition = True
    
    if condition == True:
        print("The given values satisfies 'a=b-c' or one of its variations.")
        
    formula_3(a,b,c)
    

def formula_3(a,b,c):
    '''
    Parameters: a,b,c being three input numbers.
    ----------
    
    This function checks if the input integers satisfy the product formula a*b=c or its variations.
    
    Returns: if condition == True, prints 'satisfies equation',
             else, prints nothing.
    '''
    
    condition = False
    if a*b == c:
        condition = True
    elif b*c == a:
        condition = True
    elif a*c == b:
        condition = True
    
    if condition == True:
        print("The given values satisfies 'a*b=c' or one of its variations.")
        

    
#using __name__ so that the test cases are not imported.   

if __name__ ==  '__main__':
    
    a,b,c =  1,3,4
    print(a,b,c)
    formula_1(a,b,c)
    
    print()
    
    a,b,c =  9,3,3
    print(a,b,c)
    formula_1(a,b,c)
    
    print()
    
    a,b,c = 4,1,3
    print(a,b,c)
    formula_1(a,b,c)
    
    print()
    
    a,b,c =  2,3,6
    print(a,b,c)
    formula_1(a,b,c)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
