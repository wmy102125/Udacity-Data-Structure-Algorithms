"""
Problem 4: Dutch National Flag Problem
Dutch National Flag Problem
Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal. You're not allowed to use any sorting function that Python provides.

Note: O(n) does not necessarily mean single-traversal. For e.g. if you traverse the array twice, that would still be an O(n) solution but it will not count as single traversal.

Here is some boilerplate code and test cases to start with:
"""


def sort_012(arr):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    low = 0
    mid = 0
    high = len(arr) - 1
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
            continue
        if arr[mid] == 1:
            mid += 1
            continue # this is very important ,or if arr[mid = mid+1]==2,then the numbers of loop will decrease once
        if arr[mid] == 2:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
            continue
    return arr
    # low, mid, high = 0, 0, len(arr) - 1
    #
    # while mid <= high:
    #     if arr[mid] == 0:
    #         # 交换 arr[low] 和 arr[mid]，并移动 low 和 mid
    #         arr[low], arr[mid] = arr[mid], arr[low]
    #         low += 1
    #         mid += 1
    #     elif arr[mid] == 1:
    #         # 1 已经在中间区域，直接移动 mid
    #         mid += 1
    #     else:
    #         # 交换 arr[mid] 和 arr[high]，并移动 high
    #         arr[mid], arr[high] = arr[high], arr[mid]
    #         high -= 1
    #
    # return arr


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


# test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
# test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
