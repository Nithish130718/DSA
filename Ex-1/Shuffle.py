# -*- coding: utf-8 -*-
'''
This module provides a function that shuffles a list without the usage of any built-in functions, based on an algorithm. 
This exercise comes under the course UIT2201 (Programming and Data Structures).

This is a source code purely based on my logic. It may have some bugs as well. 

Kindly feel free to comment down your suggestions and/or opinions.

Created on: 8th April 2023

Revised on: 9th April 2023

Original Author: Nithish Kumar S 
'''


import random

def shuffle(data):
    '''
    Parameters: 'data' is any input list which is a list of elemments of the same data type.
    ----------
    
    WORKS ON: Fisher-Yates Shuffle Algorithm.
    
    This 'shuffle' function accepts a list as said. To be noted that, the each element is ordered in terms of their 
    indices. It shuffles the input list and returns a shuffled list, in which the elements and their indices have now been changed, from that of the original list
    
    Returns: if 'data' has any elements, returns a shuffled list,
             if 'data' is empty, returns 'None'.
    '''

    
    length=len(data)
    
    if length==0:
        return None 

    else:
        for i in range(length-1,0,-1):
            j=random.randint(0,i)                       #parsing from the end of list
        
            data[i],data[j] = data[j],data[i]           #assigns the element to a random index generated.
        
        return data
        

#using __name__ so that the test cases are not imported.
if __name__ == '__main__':
    
    test1=[]
    print("The input list is:",test1)
    print("The shuffled list is:",shuffle(test1))
    
    print()
    
    test2=[1,2,3,4,5,6,7]
    print("The input list is:",test2)
    print("The shuffled list is:",shuffle(test2))
    
    print()
    
    test3=['A','B','C','D','E']
    print("The input list is:",test3)
    print("The shuffled list is:",shuffle(test3))
    
    print()
    
    test4=[3,5,3,4]
    print("The input list is:",test4)
    print("The shuffled list is:",shuffle(test4))
