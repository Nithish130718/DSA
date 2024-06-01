import time
import math
import random


#BUBBLESORTING ALGORITHM

def bubblesort(arr):
    start = time.time()

    global bubble_comp_count
    global bubble_swap_count
    bubble_comp_count = 0
    bubble_swap_count = 0
    n = len(arr)
    for i in range(len(arr)):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                bubble_swap_count += 1
        bubble_comp_count += n-i-1
        
    print('Number of comparisons done:',bubble_comp_count)
    print('Number of swapping executed:',bubble_swap_count)
    end = time.time()
    print('Time of execution:',end-start)
    return arr
