
from random import randrange
import time

ls = []
# for i in range(0, 15000):
#     ls.append(randrange(10000))


lpa = 15001
for i in range(0, 15000):
    lpa-=1
    ls.append(lpa)


def sorter():
    comp=0
    
    print("Iniciando!")
    print("Unsorted List:")
    print(ls)
    print(" ")
    print(" ")
    minimum = -1
    start = time.time()
    for y in range(0, len(ls)):
        troca = False
        minimum = ls[y]

        for x in range(y, len(ls)):
            comp+=1
            if (ls[x] < minimum):
                minimum = ls[x]
                xIndex = x
                troca = True
        if (troca):
            min_position = xIndex
            ls.insert(y, ls.pop(min_position))
            ls.insert(min_position, ls.pop(y+1))
    end = time.time()
    print("Sorted List:")
    print(" ")
    print(ls)
    print(f"Sorted items: {len(ls)}   |   Elapsed time:{round(end-start,2)} seconds   |   {comp} comparisons")
    # print("Sorted in ", "{0:.2f}".format(end - start), f" seconds")
sorter()
