import random
import time
ls = [10,9,8,7,6,5,4,3,2,1,0]
ls_random = []
for k in range(0,5000):
    ls_random.append(random.randint(0,100))

def bubble_sort(array):
    print("Sorting: \n", array)
    start = time.time()
    for i in range(0, len(array)):
        for j in range(0, len(array)-1):            
            if(array[j]>array[j+1]):
                temp=array[j+1]
                array[j+1]=array[j]
                array[j]=temp
    end = time.time()
    print("Sorted list: \n", array)
    print(f"Sorted items: {len(ls_random)}  |    Elapsed time:{round(end-start,2)} seconds")
    return ls

bubble_sort(ls_random)

