# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 20:13:01 2023

@author: NITHISH S
"""

class Point:
    
    '''
    This class contains 
    1. a constructor to assign (x,y) coordinate to a point.
    2. 'special methods / functions' to add, sub two points.
    '''
    
    x,y = 0,0
    
    def __init__(self,a,b):              #constructor to assign (x,y) coordinates to a point
        self.x = a
        self.y = b
        
    def __add__(self,other):             #func to add two points
        add_x = self.x + other.x
        add_y = self.y + other.y
        return (add_x,add_y)
    
    def __sub__(self,other):             #func to sub two points
        sub_x = self.x - other.x
        sub_y = self.y - other.y
        return (sub_x,sub_y)
    
    def __str__(self):                   # to print the obj instead of its memory location
        return '(' + str(self.x) + "," + str(self.y) + ")"
    

p1 = Point(4,5)
p2 = Point(3,4)

p3 = p1+p2
p4 = p1-p2

print(p3)
print(p4)