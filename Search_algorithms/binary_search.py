import time


################## Make sure the array is sorted in order to use the binary search algorithm ##################
def sorter(ls):
    start = time.time()
    print("Iniciando!")
    print("Unsorted List:")
    print(ls)
    print(" ")
    print(" ")
    minimum = -1
    counter = -1
    for y in range(0, len(ls)):
        troca = False
        counter = counter+1
        minimum = ls[y]
        for x in range(y, len(ls)):
            if (ls[x] < minimum):
                minimum = ls[x]
                xIndex = x
                troca = True

        if (troca):
            min_position = xIndex
            old_min_value = ls[y]
            ls.insert(y, ls.pop(min_position))
            ls.insert(min_position, ls.pop(y+1))
        # print(ls)
    end = time.time()
    print("Sorted List:")
    print(" ")
    print(ls)
    print("Sorted in ", "{0:.2f}".format(end - start), " seconds")
    return ls


####################################     Binary search algorithm below     ####################################

def binary_Search(array, n_search, begin=0, end=None):
    if end is None:
        end = len(array)-1
    if(begin<=end):
        middle = (begin+end)//2
        if(n_search < array[middle]):
            return binary_Search(array, n_search, begin, middle-1)
        elif(n_search > array[middle]):
            return binary_Search(array, n_search, middle+1, end)
        else:
            return middle
    return None


ls = sorter([11341,6,4,8,5,1546,153,156,47,15,5,4,7,2,8,12])
n = int(input("Digite um número para buscar no array:"))
print(binary_Search(ls, n, 0, len(ls)-1))