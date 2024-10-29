def pair_sum(arr, target):
    """
    :param: arr - input array
    :param: target - target value
    TODO: complete this method to find two numbers such that their sum is equal to the target
    Return the two numbers in the form of a sorted list
    """
    ## this function time complexity is O(n^2) the space complexity is O(n)
    if len(arr) <= 1:
        return [None,None]
    element = arr[0]
    if (target - element) in arr:
        return [element, target - element]
    else:
        return pair_sum(arr[1:], target)


def pair_sum_second_try(arr, target):
    """
    :param: arr - input array
    :param: target - target value
    TODO: complete this method to find two numbers such that their sum is equal to the target
    Return the two numbers in the form of a sorted list
    """
    sorted(arr)
    front_index = 0
    back_index = len(arr) - 1
    while (True):
        if front_index >= back_index:
            return [None, None]
        if arr[front_index] + arr[back_index] < target:
            front_index += 1
        elif arr[front_index] + arr[back_index] > target:
            back_index -= 1
        else:
            return [arr[front_index] ,arr[back_index]]

# solution
def pair_sum_solution(arr, target):
    # sort the list
    arr.sort()

    # initialize two pointer - one from start of the array and other from the end
    front_index = 0
    back_index = len(arr) - 1

    # shift the pointers
    while front_index < back_index:
        front = arr[front_index]
        back = arr[back_index]

        if front + back == target:
            return [front, back]
        elif front + back < target:  # sum < target ==> shift front pointer forward
            front_index += 1
        else:
            back_index -= 1  # sum > target ==> shift back pointer backward

    return [None, None]


def test_function(test_case):
    input_list = test_case[0]
    target = test_case[1]
    solution = test_case[2]
    output = pair_sum_second_try(input_list, target)
    if output == solution:
        print("Pass")
    else:
        print("False")


input_list = [2, 7, 11, 15]
target = 9
solution = [2, 7]
test_case = [input_list, target, solution]
test_function(test_case)

input_list = [0, 8, 5, 7, 9]
target = 9
solution = [0, 9]
test_case = [input_list, target, solution]
test_function(test_case)

input_list = [110, 9, 89]
target = 9
solution = [None, None]
test_case = [input_list, target, solution]
test_function(test_case)
