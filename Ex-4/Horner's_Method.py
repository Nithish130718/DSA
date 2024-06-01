
# -*- coding: utf-8 -*-
"""
This module provides a function that evaluates polynomial of n degree, given by
user using the O(n) Time Complexity or Aka Horner's Method. This is a part of
the exercises given under the course UIT2201 (Programming and Data Structures).

In this source code I've executed my own logic and may contain bugs. The source
code has followed good coding practices.

Your comments and suggestions are welcome.

Created on Wed Apr 27 2023

Revised on Wed May 7 2023

Original Author: Nithish Kumar S
"""


import random
def polynomial():
    '''
    This functions takes in the degree of polynomial from user
    and uses random module to create coefficients and appends
    to a list and returns the list.

    Returns : A list of coefficients
    '''
    n = int(input("Enter the degree of polynomial: "))
    coeff = []
    for i in range(n+1):
        coeffs = random.randint(1,100)
        coeff.append(coeffs)
    
    print("Coefficients are: ", coeff)
    return coeff

def getx():
    '''
    This function takes in the value of x from user
    to evaluate the polynomial.
    
    Returns the value of x to be used in main function.
    '''
    x = int(input("Enter the value of x: "))
    return x

def Horner(coeff, x):
    '''
    This function evaluates the polynomial using 
    O(n) Time complexity. 

    Takes in list and value of x as arguments.

    Returns the final evaluated value of the created polynomial.
    '''
    fn = 0
    n = len(coeff)
    result = coeff[0]
    for i in range(1,n):
        fn += 1
        result = result * x + coeff[i]
    
    print("f(n) for Horner's method of degree", n, "is:", fn)
    return result

#Running the above program.
print(Horner(polynomial(), getx()))
