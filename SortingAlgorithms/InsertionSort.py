
#INSERTION SORT ALGORITHM

def insertion_sort(arr):
    global is_comp_count
    is_comp_count = 0
    start3 = time.time()
    n = len(arr)
    for i in range(1,n):
        temp = arr[i]
        j=i-1
        while j>=0 and arr[j]>temp:
            is_comp_count+=1
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = temp
        
    print('Number of comparisons done:',is_comp_count)
    end3 = time.time()
    print('Time of execution is:',end3-start3)
    return arr


if __name__ == '__main__':
    list1 = []
    n = int(input("Enter the number of elements:"))
    for i in range(n):
        ele = random.randint(-100,100)
        list1.append(ele)
    
    print('The original list is:',list1)

    print('\n INSERTION SORTING: \n')
    is_res = insertion_sort(list3)
    print('The insertion sorting sorted list is:',list1)
    print('n value:',is_comp_count / n)
    print('n^2 value:',is_comp_count / n**2)
    print('n^3 value:',is_comp_count / n**3)
    print('logn value:',is_comp_count / math.log(n))

