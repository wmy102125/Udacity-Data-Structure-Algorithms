"""
You are given an array `arr` having `n` integers. You have to find the maximum sum of contiguous subarray among all the possible subarrays. This problem is commonly called as [Maximum Subarray Problem](https://en.wikipedia.org/wiki/Maximum_subarray_problem). Solve this problem in *O(nlogn)* time, using Divide and Conquer approach.


**Example 1**<br>
Input: `arr = [-2, 1, -3, 5, 0, 3, 2, -5, 4]`<br>
Output: `Maximum Sum = 10` for the  `subarray = [5, 0, 3, 2]`<br>

**Example 2**<br>
Input: `arr = [-2, -5, 6, -2, -3, 1, 5, -6]`<br>
Output: `Maximum Sum = 7`  for the  `subarray = [6, -2, -3, 1, 5]`<br>

***As of now, let's not return the subarray itself.***
"""
from pyparsing import nums


def maxSubArray_common(arr):
    '''
    param: An array `arr`
    return: The maximum sum of the contiguous subarray.
    No need to return the subarray itself.
    '''
    current_sum = arr[0]
    max_sum = arr[0]
    for num in arr[1:]:
        current_sum = max(current_sum + num, num)
        max_sum = max(current_sum, max_sum)
    return max_sum


# Test your code
arr = [-2, 7, -6, 3, 1, -4, 5, 7]
print("Maximum Sum = ", maxSubArray_common(arr))  # Outputs 13


def maxSubArray_mine(arr):

    pass
def _max_sub_array_mine(arr, startIndex, endIndex):
    if startIndex >= endIndex:
        return arr[startIndex]
    mid = len(arr) // 2
    left_max = _max_sub_array_mine(arr, startIndex, mid)
    right_max = _max_sub_array_mine(arr, mid, endIndex)


# Solution

'''Helper Function - Find the max crossing sum w.r.t. middle index'''


def maxCrossingSum(arr, start, mid, stop):
    '''LEFT PHASE - Traverse the Left part starting from mid element'''
    leftSum = arr[mid]  # Denotes the sum of left part from mid element to the current element
    leftMaxSum = arr[mid]  # Keep track of maximum sum

    # Traverse in reverse direction from (mid-1) to start
    for i in range(mid - 1, start - 1,
                   -1):  # The second argument of range is not inclusive. Third argument is the step size.
        leftSum = leftSum + arr[i]
        if (leftSum > leftMaxSum):  # Update leftMaxSum
            leftMaxSum = leftSum

    '''RIGHT PHASE - Traverse the Right part, starting from (mid+1)'''
    rightSum = arr[mid + 1]  # Denotes the sum of right part from (mid+1) element to the current element
    rightMaxSum = arr[mid + 1]  # Keep track of maximum sum

    # Traverse in forward direction from (mid+2) to stop
    for j in range(mid + 2, stop + 1):  # The second argument of range is not inclusive
        rightSum = rightSum + arr[j]
        if (rightSum > rightMaxSum):  # Update rightMaxSum
            rightMaxSum = rightSum

    '''Both rightMaxSum and lefttMaxSum each would contain value of atleast one element from the arr'''
    return (rightMaxSum + leftMaxSum)


'''Recursive function'''


def maxSubArrayRecursive(arr, start, stop):  # start and stop are the indices
    # Base case
    if (start == stop):
        return arr[start]

    if (start < stop):
        mid = (start + stop) // 2  # Get the middle index
        L = maxSubArrayRecursive(arr, start, mid)  # Recurse on the Left part
        R = maxSubArrayRecursive(arr, mid + 1, stop)  # Recurse on the Right part
        C = maxCrossingSum(arr, start, mid, stop)  # Find the max crossing sum w.r.t. middle index
        return max(C, max(L, R))  # Return the maximum of (L,R,C)

    else:  # If ever start > stop. Not feasible.
        return nums[start]


def maxSubArray(arr):
    start = 0  # staring index of original array
    stop = len(arr) - 1  # ending index of original array
    return maxSubArrayRecursive(arr, start, stop)


# Test your code
arr = [-2, 7, -6, 3, 1, -4, 5, 7]
print("Maximum Sum = ", maxSubArray(arr))  # Outputs 13

# Test your code
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print("Maximum Sum = ", maxSubArray(arr))  # Outputs 6

# Test your code
arr = [-4, 14, -6, 7]
print("Maximum Sum = ", maxSubArray(arr))  # Outputs 15

# Test your code
arr = [-2, 1, -3, 5, 0, 3, 2, -5, 4]
print("Maximum Sum = ", maxSubArray(arr))  # Outputs 10

# Test your code
arr = [-2, -5, 6, -2, -3, 1, 5, -6]
print("Maximum Sum = ", maxSubArray(arr))  # Outputs 7
