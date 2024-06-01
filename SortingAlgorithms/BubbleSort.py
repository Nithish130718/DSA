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

if __name__ == '__main__':
    list1 = []
    n = int(input("Enter the number of elements:"))
    for i in range(n):
        ele = random.randint(-100,100)
        list1.append(ele)
        
    print('The original list is:',list1)

    print('\n BUBBLE SORTING: \n')
    bubble_res = bubblesort(list1)
    print('The bubble sorted list is:',list1)
    print('n^2 value:',bubble_comp_count / n**2)
    print('n^3 value:',bubble_comp_count / n**3)
    print('logn value:',bubble_comp_count / math.log(n))
