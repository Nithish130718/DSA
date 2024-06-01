# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 20:19:50 2023

@author: NITHISH S
"""

class Rational:
    
    '''
    This class contains,
    1. __init__ constructor to to check if its a valid rational number. If valid - assign nr,dr. Else,return error
    2. 'special methods / functions' to add, sub, mul, div, invert rational numbers.
    '''
    
    n=0
    d=1
    
    def __init__(self,num,den):
        
        if den == 0:
            raise ZeroDivisionError("Denominator of a rational number cannot be zero!")
        
        x = isinstance(num,int)
        y = isinstance(den,int)
        
        if y == False:
            raise TypeError("Denominator is not int value")
            
        if x == False:
            raise TypeError("Numerator is not int value.")
            
        if x and y == True:
            if den>0:                          #sign convention using if-else to write -ve sign on nr if dr is -ve.
                self.n = num
                self.d = den
            else:
                self.n = num * (-1)
                self.d = den * (-1)
            
    
    def __add__(self,other):                   #adding two rational numbers
        nr1 = self.n * other.d
        nr2 = other.n * self.d
        dr = self.d * other.d
        return Rational((nr1+nr2),dr)
    
    
    def __sub__(self,other):                  #subtracting two rational numbers
        nr1 = self.n * other.d
        nr2 = other.n * self.d
        dr = self.d * other.d
        return Rational((nr1-nr2),dr)
    
    
    def __mul__(self,other):                  #multiplying two rational numbers
        nr = self.n * other.n
        dr = self.d * other.d
        return Rational(nr,dr)
    
    
    def __truediv__(self,other):             #dividing one rational number by another
        nr = self.n * other.d                #results like (a/b) / (c/d)  =  a/b * d/c
        dr = self.d * other.n                
        return Rational(nr,dr)
        
    
    def __invert__(self):                    #taking reciprocal of a rational number
        self.n,self.d = self.d,self.n
        return Rational(self.n,self.d)
     
    
    def __str__(self):                       #using __str__ to print the obj and not its memory
        return str(self.n) + "/" + str(self.d)
            


r1 = Rational(3,4)
r2 = Rational(4,5)

r3 = r1+r2
print(r3)

r4 = r1-r2
print(r4)

r5 = r1*r2
print(r5)

r6 = r1/r2
print(r6)

print(r1.__invert__())

            
            

            
        