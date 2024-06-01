# -*- coding: utf-8 -*-
'''
This module provides a function that finds the minmax of a list, which consists of elements of the same data type. 
This exercise comes under the course UIT2201 (Programming and Data Structures).

This is a source code purely based on my logic. It may have some bugs as well. 

Kindly feel free to comment down your suggestions and/or opinions.

Created on: 8th April 2023

Revised on: 9th April 2023

Original Author: Nithish Kumar S 
'''


def minmax(data):
    '''
    Parameters: 'data' is any input list which consists of elements of the same type.
    ----------
    
    This minmax function finds the minimuum and maximum of a list and prints it.

    Returns: if 'data'  list is empty, returns none.
             if 'data' has only one element, retuns that element as 'maximum and minimum'
    '''
    
    length=len(data)
    if length==0:
        return None
    elif length==1:
        return(data[0],data[0])
    elif length==2:
        if data[0]<data[1]:
            return(data[0],data[1])
        else:
            return(data[1],data[0])
    else:
        for i in range(length):
            for j in range(length-i-1):
                if data[j]>data[j+1]:
                    data[j],data[j+1] = data[j+1],data[j]
        return(data[0],data[length-1])
    

import random

def create_list(size,low=-100000,high=100000):
    '''
    Parameters: size, low and high value as keyword arguments.
    ----------
    
    size : given as input
    low : Lowest value that can be present. The default is -100000.
    high : Highest value that can be present. The default is 100000.

    
    Returns: a random list created of the desired size (passed as argument) between the lowest and the highest values.
    '''
    
    random_list=[]
    for i in range(size):
        random_list.append(random.randint(low,high))
    return random_list



size=int(input("Enter the desired size of the list:"))

random_list = create_list(size)

func_answer = minmax(random_list)


#checking if minmax function returned the right answer

length=len(random_list)

if length==0:
    right_answer = None
else:
    right_answer = (min(random_list),max(random_list))
    print("func answer=",func_answer,"\n","right answer=",right_answer)
    if func_answer!=right_answer:
        raise Exception("The minmax function didn't return a correct answer!")
    
        


#using __name__ so that the test cases are not imported.

if __name__ == '__main__':
    
    print() 
    
    test1=()
    print(minmax(test1))
    
    print()

    test2=["Nithish"]
    print(minmax(test2))
    
    print()

    test3=["Nithish","Karthik","Daniel","Goutham"]
    print(minmax(test3)) 
        
    print()
    
    
    
    
