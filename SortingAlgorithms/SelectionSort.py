
import time
import math
import random

def selection_sort(arr):
    start2 = time.time()
    global ss_comp_count
    global ss_swap_count
    ss_comp_count = 0
    ss_swap_count = 0
    
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1,len(arr)):
            ss_comp_count+=1
            if arr[j]<arr[min_index]:
                min_index = j
        if i!=min_index:
            arr[i],arr[min_index] = arr[min_index],arr[i]
            ss_swap_count += 1
            
    print('Number of comparisons done:',ss_comp_count)
    print('Number of swapping executed:',ss_swap_count)
    end2 = time.time()
    print('Time of execution is:',end2-start2)
    return arr

if __name__ == '__main__':
    list1 = []
    n = int(input("Enter the number of elements:"))
    for i in range(n):
        ele = random.randint(-100,100)
        list1.append(ele)
    
    print('The original list is:',list1)

    print('\n SELECTION SORTING: \n')
    ss_res = selection_sort(list2)
    print('The selection sorted list is:',list1)
    print('n^2 value:',ss_comp_count / n**2)
    print('n^3 value:',ss_comp_count / n**3)
    print('logn value:',ss_comp_count / math.log(n))

