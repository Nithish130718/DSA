import random
from random import randint
import time
from math import log 

# Merge sort 

def merge(A,B):                 
    result = []
    m = len(A)
    n = len(B)
    i = j = 0
    while i<m and j<n:
        if A[i]<B[j]:
            result.append(A[i])
            i+=1
            
        else:
            result.append(B[j])
            j+=1

    while i<m:
        result.append(A[i])
        i+=1
    while j<n:
        result.append(B[j])
        j+=1

    return result
    

def msort(list):
    n = len(list)
    if n<2:
        return list[:]
    else:
        mid = n//2
        return merge(msort(list[:mid]),msort(list[mid:]))


if __name__ == '__main__':
    #Merge sort
    n = int(input("Enter the number of elements:"))
    list = []
    for i in range(n):
        list.append(random.randint(-100,100))
    print('The original list is:',list)
    print('List after sorting is:',msort(list))
