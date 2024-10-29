"""
Problem Statement
Write a function that takes an input array (or Python list) consisting of only 0s, 1s, and 2s, and sorts that array in a single traversal.

Note that if you can get the function to put the 0s and 2s in the correct positions, this will automatically cause the 1s to be in the correct positions as well.
"""


def sort_012(input_list):
    back_index = _sort_012(input_list, 2, 0, len(input_list) - 1)
    _sort_012(input_list, 1, 0, back_index)


def _sort_012(input_list, target, target_index, back_index):
    if target_index >= back_index:
        return back_index
    if input_list[target_index] == target:
        if input_list[back_index] == target:
            back_index -= 1
        else:
            input_list[target_index], input_list[back_index] = input_list[back_index], input_list[target_index]
            target_index += 1
            back_index -= 1
    else:
        target_index += 1
    return _sort_012(input_list, target, target_index, back_index)


def sort_012_second_try(input_list):
    target_index = 0
    next_0 = 0
    next_2 = len(input_list) - 1
    while target_index <= next_2:
        if input_list[target_index] == 2:
            input_list[target_index], input_list[next_2] = input_list[next_2], input_list[target_index]
            next_2 -= 1
        elif input_list[target_index] == 0:
            input_list[target_index], input_list[next_0] = input_list[next_0], input_list[target_index]
            target_index += 1
            next_0 += 1
        else :
            target_index += 1

def test_function(test_case):
    sort_012_second_try(test_case)
    print(test_case)
    if test_case == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


test_case = [0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2]
test_function(test_case)

test_case = [2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1]
test_function(test_case)

test_case = [2, 2, 0, 0, 2, 1, 0, 2, 2, 1, 1, 1, 0, 1, 2, 0, 2, 0, 1]
test_function(test_case)
