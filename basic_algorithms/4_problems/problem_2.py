"""
Problem 2: Search in a Rotated Sorted Array
Search in a Rotated Sorted Array
You are given a sorted array which is rotated at some random pivot point.

Example: [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]

You are given a target value to search. If found in the array return its index, otherwise return -1.

You can assume there are no duplicates in the array and your algorithm's runtime complexity must be in the order of O(logn).

Example:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Here is some boilerplate code and test cases to start with:
"""


def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    mid_index = len(input_list) // 2
    pivot = input_list[mid_index]
    if number == pivot:
        return len(input_list) // 2
    # arr[0]<n<pivot ,recursive the left of the array
    if number >= input_list[0]:
        return _rotated_array_search(input_list, number, 0, mid_index - 1)
    # n<arr[last_index],recursive the right of the array
    if number <= input_list[len(input_list) - 1]:
        return _rotated_array_search(input_list, number, mid_index + 1, len(input_list) - 1)


def _rotated_array_search(input_list, number, start_index, end_index):
    if start_index >= end_index:
        if input_list[start_index] == number:
            return start_index
        else:
            return -1
    mid_index = (start_index + end_index) // 2
    pivot = input_list[mid_index]
    if number == pivot:
        return mid_index
    if number < pivot:
        return _rotated_array_search(input_list, number, start_index, mid_index - 1)
    else:
        return _rotated_array_search(input_list, number, mid_index + 1, end_index)


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


# test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
# test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
# test_function([[6, 7, 8, 1, 2, 3, 4], 1])
# test_function([[6, 7, 8, 1, 2, 3, 4], 10])
