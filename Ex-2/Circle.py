# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 20:08:49 2023

@author: NITHISH S
"""

class Circle: 
    
    radius = 0
    
    def __init__ (self,r):                  #constructor to assign radius value
        self.radius = r
        
    def area(self):                         #returns area
        sq = self.radius * self.radius
        area_circle = 3.14 * sq
        return area_circle
    
    def perimeter(self):                    #returns perimeter
        perimeter_circle = 2 * 3.14 * self.radius
        return perimeter_circle
    

data1=Circle(5)
data2=Circle(3)

print(data1.area())
print(data2.area())

print(data1.perimeter())
print(data2.perimeter())