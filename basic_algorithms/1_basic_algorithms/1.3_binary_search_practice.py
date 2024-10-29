def binary_search(array, target):
    '''Write a function that implements the binary search algorithm using iteration

    args:
      array: a sorted array of items of the same type
      target: the element you're searching for

    returns:
      int: the index of the target, if found, in the source
      -1: if the target is not found
    '''
    arr_length = len(array)
    if arr_length == 1:
        if array[0] == target:
            return 0
        else:
            return -1
    mid_index = get_middle_index(arr_length)
    while mid_index < len(array) - 1 or mid_index > 0:
        arr_length = len(array[mid_index + 1:])
        if array[mid_index] < target:
            mid_index += get_middle_index(arr_length)
        elif array[mid_index] > target:
            mid_index -= get_middle_index(arr_length)
        else:
            return mid_index

    return -1


def get_middle_index(arr_length):
    if arr_length == 2:
        return 1
    mod = arr_length % 2
    if mod == 0:
        return (arr_length // 2) - 1
    else:
        return arr_length // 2


def binary_search_solution(array, target):
    start_index = 0
    end_index = len(array) - 1

    while start_index <= end_index:
        mid_index = (start_index + end_index) // 2  # integer division in Python 3

        mid_element = array[mid_index]

        if target == mid_element:  # we have found the element
            return mid_index

        elif target < mid_element:  # the target is less than mid element
            end_index = mid_index - 1  # we will only search in the left half

        else:  # the target is greater than mid element
            start_index = mid_element + 1  # we will search only in the right half

    return -1

def test_function(test_case):
    answer = binary_search(test_case[0], test_case[1])
    if answer == test_case[2]:
        print("Pass!")
    else:
        print("Fail!")


array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 6
index = 6
test_case = [array, target, index]
test_function(test_case)


def binary_search_recursive(array, target):
    '''
    This function will call `binary_search_recursive_soln` function.
    You don't need to change this function.

    args:
      array: a sorted array of items of the same type
      target: the element you're searching for
    '''
    return binary_search_recursive_soln(array, target, 0, len(array) - 1)


def binary_search_recursive_soln(array, target, start_index, end_index):
    '''Write a function that implements the binary search algorithm using recursion

    args:
      array: a sorted array of items of the same type
      target: the element you're searching for
      start_index: beginning of the index of the sub-arrays
      end_index: end of the index of the sub-arrays

    returns:
      int: the index of the target, if found, in the source
      -1: if the target is not found
    '''
    if end_index == 0:
        if array[0] == target:
            return 0
        else:
            return -1
    mid_index = get_middle_index(end_index + 1)
    if target > array[mid_index]:
        binary_search_recursive_soln(array[mid_index:], target, 0, len(array[mid_index:]) - 1)
    elif target < array[mid_index]:
        binary_search_recursive_soln(array[0:mid_index], target, 0, mid_index)
    else:
        return mid_index


def binary_search_recursive_soln_solution(array, target, start_index, end_index):
    if start_index > end_index:
        return -1

    mid_index = (start_index + end_index) // 2
    mid_element = array[mid_index]

    if mid_element == target:
        return mid_index
    elif target < mid_element:
        return binary_search_recursive_soln(array, target, start_index, mid_index - 1)
    else:
        return binary_search_recursive_soln(array, target, mid_index + 1, end_index)

def test_function(test_case):
    answer = binary_search_recursive(test_case[0], test_case[1])
    if answer == test_case[2]:
        print("Pass!")
    else:
        print("Fail!")
array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 4
index = 4
test_case = [array, target, index]
test_function(test_case)
