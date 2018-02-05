# Bubble Sort 

#
# Run time of O(n^2) by many considerations a slow sorting algorithum   
#

# the outer loop controls the number of passes needed to sort everything. The number of passes need is the lenght of the list - 1
def bubbleSort(mylist):
    for i in range(0, len(mylist)-1):
        #innter loop is moving the buble along
        for j in range(0, len(mylist)-1):
            if mylist[j] > mylist[j+1]:
                mylist[j], mylist[j+1] = mylist[j+1], mylist[j]
    return mylist

ex_list = [1, 12, 6, 8, 9, 14]
print(bubbleSort(ex_list))
