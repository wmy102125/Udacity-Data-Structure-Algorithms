"""
Binary Search¶
Overview
Given a sorted list (say arr), and a key (say target). The binary search algorithm returns the index of the target element if it is present in the given arr list, else returns -1. Here is an overview of how the the recursive version of binary search algorithm works:

Given a list with the lower bound (start_index) and the upper bound (end_index).
Find the center (say mid_index) of the list.
Check if the element at the center is your target? If yes, return the mid_index.

Check if the target is greater than that element at mid_index? If yes, call the same function with right sub-array w.r.t center i.e., updated indexes as mid_index + 1 to end_index

Check if the target is less than that element at mid_index? If yes, call the same function with left sub-array w.r.t center i.e., updated indexes as start_index to mid_index - 1

Repeat the step above until you find the target or until the bounds are the same or cross (the upper bound is less than the lower bound).
"""
"""Complexity Analysis¶
Let's look at the time complexity of the recursive version of binary search algorithm.

Note: The binary search function can also be written iteratively. But for the sake of understanding recurrence relations, we will have a look at the recursive algorithm.

Here's the binary search algorithm, coded using 4_recursion:"""
def binary_search(arr, target):
    return _binary_search(arr, 0, len(arr) - 1, target)


def _binary_search(arr, start_index, end_index, target):
    if end_index < start_index or end_index > len(arr) - 1:
        return -1
    mid_index = (start_index + end_index) // 2
    if arr[mid_index] == target:
        return arr[mid_index]
    if arr[mid_index] > target:
        return _binary_search(arr, start_index, mid_index - 1, target)
    if arr[mid_index] < target:
        return _binary_search(arr, mid_index + 1, end_index, target)


def binary_search_solution(arr, target):
    return binary_search_func_solution(arr, 0, len(arr) - 1, target)


def binary_search_func_solution(arr, start_index, end_index, target):
    if start_index > end_index:
        return -1

    mid_index = (start_index + end_index) // 2

    if arr[mid_index] == target:
        return mid_index
    elif arr[mid_index] > target:
        return binary_search_func_solution(arr, start_index, mid_index - 1, target)
    else:
        return binary_search_func_solution(arr, mid_index + 1, end_index, target)


arr = [0, 1, 2, 3, 4, 5, 6, 7, 8]
print(binary_search(arr, 9))

"""𝑇(𝑛)=𝑙𝑜𝑔(𝑛)∗𝑘

Thus we see that the time complexity of the function is a logarithmic function of the input, 𝑛
. Hence, the time complexity of the recursive algorithm for binary search is 𝑙𝑜𝑔(𝑛)
.Our binary_search() function calls the binary_search_func() function. So the time complexity of the function is entirely dependent on the time complexity of the binary_search_func().

The input here is an array, so our time complexity will be determined in terms of the size of the array.

Like we did earlier, let's say the time complexity of binary_search_func() is a function of the input size, n. In other words, the time complexity is  𝑇(𝑛)
 .

Also keep in mind that we are usually concerned with the worst-case time complexity, and that is what we will calculate here. In the worst case, the target value will not be present in the array.

In the binary_search_func() function, we first check for the base case. If the base case does not return True, we calculate the mid_index and then compare the element at this mid_index with the target values. All the operations are independent of the size of the array. Therefore, we can consider all these independent operations as taking a combined time,  𝑘
 .

Apart from these constant time operations, we do just one other task. We either make a call on the left-half of the array, or on the right half of the array. By doing so, we are reducing the input size by  𝑛/2
 .

Note: Remember that we usually consider large input sizes while calculating time complexity; there is no significant difference between  105
  and ( 105+1
 ).

Thus, our new function call is only called with half the input size. We said that  𝑇(𝑛)
  was the time complexity of our original function. The time complexity of the function when called with half the input size will be  𝑇(𝑛/2)
 .

Therefore:

𝑇(𝑛)=𝑇(𝑛/2)+𝑘
 

Similarly, in the next step, the time complexity of the function called with half the input size would be:

𝑇(𝑛/2)=𝑇(𝑛/4)+𝑘
 

We can now form similar equations as we did for the last problem:

𝑇(𝑛)   =𝑇(𝑛/2)+𝑘
 
𝑇(𝑛/2)=𝑇(𝑛/4)+𝑘
 
𝑇(𝑛/4)=𝑇(𝑛/8)+𝑘
 
𝑇(𝑛/8)=𝑇(𝑛/16)+𝑘
  .
.
.
.
.
.
𝑇(4)=𝑇(2)+𝑘
 
𝑇(2)=𝑇(1)+𝑘
 
𝑇(1)=𝑇(0)+𝑘1
   (1)
 
𝑇(0)=𝑘1
 
(1)
  If we have only one element, we go to 0 elements next

From our binary search section, we know that it takes  𝑙𝑜𝑔(𝑛)
  steps to go from  𝑇(𝑛)
  to  1
 . Therefore, when we add the corresponding left-hand sides and right-hand sides, we can safely say that:"""
