import time as t


#--------------------------------------
#Merge Sort Algorithm
#--------------------------------------
def merge_sort(arr):
    global merge_comparisons
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    global merge_comparisons

    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        merge_comparisons += 1
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result



def isSorted(anArray):
    # Check if the array is sorted in ascending order
    for i in range(1, len(anArray)):
        if anArray[i - 1] > anArray[i]:
            return False

    return True



#-----------------------------
#Reading data from a txt file
#-----------------------------
def read_data(filename):
    with open(filename, 'r') as file:
        data =[int(num) for line in file for num in line.split()]
    return data


#"data/rand1000.txt"
#"data/rand10000.txt"
#"data/rand100000.txt"
#"data/rand1000000.txt"
#"data/rand250000.txt"
#"data/500000.txt"

fileNames= ["rand1000000.txt"]

for name in fileNames:
    data = read_data("data/" + name)



    #Merge Sort
    merge_data = data.copy()
    merge_comparisons = 0
    start_time = t.time()
    merge_data = merge_sort(merge_data)
    end_time = t.time()
    merge_time = end_time - start_time


    print("Merge Sort:")
    print("Time: ", merge_time)
    print("Comparisons:", merge_comparisons)
    print("Sorted:", isSorted(merge_data))