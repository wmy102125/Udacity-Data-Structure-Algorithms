"""
Problem 3: Rearrange Array Digits
Rearrange Array Elements
Rearrange array elements so as to form two number such that their sum is maximum. Return these two numbers. You can assume that all array elements are in the range [0, 9]. The number of digits in both the numbers cannot differ by more than 1. You're not allowed to use any sorting function that Python provides and the expected time complexity is O(nlog(n)).

For example, if [1, 2, 3, 4, 5] is given, the expected answer would be [531, 42]. Another expected answer can be [542, 31]. In scenarios such as these when there are more than one possible answers, return any one.

Here is some boilerplate code and test cases to start with:
"""

def rearrange_digits(input_list):
    """
    Rearranges the elements of the given array to form two numbers such that their sum is maximized.
    The numbers formed have a number of digits differing by no more than one.

    Args:
        input_list (List[int]): A list of integers

    Returns:
        Tuple[int, int]: A tuple containing two integers
    """
    if len(input_list) == 0 or len(input_list) == 1:
        return input_list
    sorted_list = quick_desc_sort(input_list)
    digits_one = ""
    digits_two = ""
    for index, value in enumerate(sorted_list):
        if index % 2 == 0:
            digits_one += str(value)
        else:
            digits_two += str(value)
    return [int(digits_one), int(digits_two)]


def quick_desc_sort(arr):
    if len(arr) == 1:
        return arr
    pivot = arr[-1]
    equal_pivot = []
    left_arr = []
    right_arr = []
    for i in arr:
        if i == pivot:
            equal_pivot.append(pivot)
        elif i > pivot:
            left_arr.append(i)
        else:
            right_arr.append(i)
    if len(left_arr) > 1:
        left_arr = quick_desc_sort(left_arr)
    if len(right_arr) > 1:
        right_arr = quick_desc_sort(right_arr)
    return left_arr + equal_pivot + right_arr


def quick_sort_second(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    equal_pivot = []
    left_arr = []
    right_arr = []
    for i in arr:
        if i == pivot:
            equal_pivot.append(pivot)
        elif i < pivot:
            left_arr.append(i)
        else:
            right_arr.append(i)
    return quick_sort_second(left_arr) + equal_pivot + quick_sort_second(right_arr)


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_case_1 = [[1, 2, 3, 4, 5], [542, 31]]
test_function(test_case_1)
test_case2 = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_function(test_case2)
test_case2 = [[0, 6, 2, 5, 9, 8], [962, 850]]
test_function(test_case2)
