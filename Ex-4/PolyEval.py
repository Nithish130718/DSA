# -*- coding: utf-8 -*-
"""
This module provides a function that evaluates polynomial of n degree, given by
user using the O(nlogn) Time Complexity. This is a part of the exercises given
under the course UIT2201 (Programming and Data Structures).

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

def power(x, y):
    '''
    The given function calculates the value of x raised
    to the power y in time O(logn).

    The input is not modified in any way and there are no
    side effects.

    args:
        x: the base
        y: the power

    Returns:
        Value of x raised to the power y.
    
    '''

    fn = 0

    fn += 1

    if(y == 0):
        return 1
    temp = power(x, int(y / 2))
    if (y % 2 == 0):
        return temp * temp
    else:
        return x * temp * temp


def polyeval(coeff, x):
    '''
    This function evaluates the polynomial using 
    O(nlogn) Time complexity. 

    Takes in list and value of x as arguments.

    Returns the final evaluated value of the created polynomial.
    '''
    fn = 0
    degree = len(coeff) - 1
    total_sum = 0
    for coeffs in coeff:
        fn += 1
        prod = power(x,degree)
        total_sum += prod*coeffs
        degree -= 1

    print("f(n):", fn)
    return total_sum

#Running the above program.
print(polyeval(polynomial(), getx())) 
