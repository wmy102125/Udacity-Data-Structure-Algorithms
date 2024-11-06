"""
Given an unsorted array Arr with n positive integers. Find the  𝑘𝑡ℎ
  smallest element in the given array, using Divide & Conquer approach.

Input: Unsorted array Arr and an integer k where  1≤𝑘≤𝑛

Output: The  𝑘𝑡ℎ
  smallest element of array Arr

Example 1
Arr = [6, 80, 36, 8, 23, 7, 10, 12, 42, 99]
k = 10
Output = 99

Example 2
Arr = [6, 80, 36, 8, 23, 7, 10, 12, 42, 99]
k = 5
Output = 12

"""
import math


def fastSelect_mine(arr, k):
    '''TO DO'''
    # Implement the algorithm explained above to find the k^th largest element in the given array
    sorted_mid = []
    group_numbers = math.ceil(len(arr) / 5)
    for i in range(group_numbers):
        g = arr[i * 5:(i + 1) * 5 - 1]
        if i == group_numbers:
            g = arr[i * 5:]
        sorted_mid.append(sort_group_mid(g))
    if len(sorted_mid) == 1:
        pivot = sorted_mid[0]
    else:
        pivot = fastSelect_mine(sorted_mid, len(sorted_mid) // 2)
    # divide the origin array to 3 groups
    arr_less_p = []
    arr_equal_p = []
    arr_larger_p = []
    for element in arr:
        if element < pivot:
            arr_less_p.append(element)
        elif element > pivot:
            arr_larger_p.append(element)
        else:
            arr_equal_p.append(element)

    if k < len(arr_less_p):
        return fastSelect_mine(arr_less_p, k)
    elif k > len(arr_less_p) + len(arr_equal_p):
        return fastSelect_mine(arr_larger_p, k - len(arr_less_p) - len(arr_equal_p))
    else:
        return pivot


def sort_group_mid(arr):
    sorted(arr)
    return arr[len(arr) // 2]


#Arr = [6, 80, 36, 8, 23, 7, 10, 12, 42]
#k = 5
#print(fastSelect_mine(Arr, k))  # Outputs 12

Arr = [5, 2, 20, 17, 11, 13, 8, 9, 11]
k = 5
print(fastSelect_mine(Arr, k))        # Outputs 11
Arr = [6, 80, 36, 8, 23, 7, 10, 12, 42, 99]
k = 10
print(fastSelect_mine(Arr, k))        # Outputs 99
# solution
def fastSelect(Arr, k):  # k is an index
    n = len(Arr)  # length of the original array

    if (k > 0 and k <= n):  # k should be a valid index
        # Helper variables
        setOfMedians = []
        Arr_Less_P = []
        Arr_Equal_P = []
        Arr_More_P = []
        i = 0

        # Step 1 - Break Arr into groups of size 5
        # Step 2 - For each group, sort and find median (middle). Add the median to setOfMedians
        while (i < n // 5):  # n//5 gives the integer quotient of the division
            median = findMedian(Arr, 5 * i, 5)  # find median of each group of size 5
            setOfMedians.append(median)
            i += 1

        # If n is not a multiple of 5, then a last group with size = n % 5 will be formed
        if (5 * i < n):
            median = findMedian(Arr, 5 * i, n % 5)
            setOfMedians.append(median)

        # Step 3 - Find the median of setOfMedians
        if (len(setOfMedians) == 1):  # Base case for this task
            pivot = setOfMedians[0]
        elif (len(setOfMedians) > 1):
            pivot = fastSelect(setOfMedians, (len(setOfMedians) // 2))

        # Step 4 - Partition the original Arr into three sub-arrays
        for element in Arr:
            if (element < pivot):
                Arr_Less_P.append(element)
            elif (element > pivot):
                Arr_More_P.append(element)
            else:
                Arr_Equal_P.append(element)

        # Step 5 - Recurse based on the sizes of the three sub-arrays
        if (k <= len(Arr_Less_P)):
            return fastSelect(Arr_Less_P, k)

        elif (k > (len(Arr_Less_P) + len(Arr_Equal_P))):
            return fastSelect(Arr_More_P, (k - len(Arr_Less_P) - len(Arr_Equal_P)))

        else:
            return pivot

        # Helper function


def findMedian(Arr, start, size):
    myList = []
    for i in range(start, start + size):
        myList.append(Arr[i])

        # Sort the array
    myList.sort()

    # Return the middle element
    return myList[size // 2]


Arr = [6, 80, 36, 8, 23, 7, 10, 12, 42]
k = 5
print(fastSelect(Arr, k))        # Outputs 12
Arr = [5, 2, 20, 17, 11, 13, 8, 9, 11]
k = 5
print(fastSelect(Arr, k))        # Outputs 11
Arr = [6, 80, 36, 8, 23, 7, 10, 12, 42, 99]
k = 10
print(fastSelect(Arr, k))        # Outputs 99



