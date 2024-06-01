import random
import time 
import math 

def find_median(list):
    n = len(list)
    start,mid,end = list[0],list[n//2],list[n-1]
    L = [start,mid,end]

    if start>mid:
        L[0],L[1] = L[1],L[0]
    if end<mid:
        L[2],L[1] = L[1],L[2]
    if start>end:
        L[0],L[2] = L[2],L[0] 
    
    return L[2]

def partition(list,begin,end):
    list = list
    i = begin
    j = end - 1
    pivot = find_median(list)

    while i<=j:
        while list[i]<=pivot and i<end:
            i+=1
        while list[j]>pivot and j>=begin:
            j-=1
        if i<j:
            list[i],list[j] = list[j],list[i]
            i+=1
            j-=1
    if i<end:
        list[i],list[end] = list[end],list[i]
    return i
    

def qsort(list,begin,end):
    if begin<end:
        k = partition(list,begin,end)
        qsort(list,begin,k-1)
        qsort(list,k+1,end)
        return list 
    else:
        return list[:]


if __name__ == '__main__':
    n = int(input("Enter the number of elements in the list:"))
    start =  time.time()
    list = [random.randint(-n,n) for i in range(n)]   
    print('The original list is:',list)

    begin = 0
    end = len(list)-1   

    res = qsort(list,begin,end)

    print('The sorted list is:',res)
    end = time.time()

    print('The time of execution is:',end-start)

    f_n = 0.455                    #Average time for 5 trials entered here.

    print('f(n)/n:',f_n/n)
    print('f(n)/n^2:',f_n/(n**2))
    print('f(n)/n^3:',f_n/(n**3))
    print('f(n)/nlogn:',f_n / (n * math.log(n,2)))


