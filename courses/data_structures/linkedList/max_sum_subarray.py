def max_sum_subarray_wmy(arr):
    """
    :param - arr - input array
    return - number - largest sum in contiguous subarry within arr
    """
    max_sum = 0
    for i in range(len(arr)):
        sum_subarray = _max_sum_subarray(arr[i:])
        if sum_subarray > max_sum:
            max_sum = sum_subarray
    return max_sum
    pass


def _max_sum_subarray(subArr):
    if subArr is None or len(subArr) == 0:
        return
    max_sum_subarray = 0
    current_sum = 0
    for item in subArr:
        current_sum = current_sum + item
        if current_sum > max_sum_subarray:
            max_sum_subarray = current_sum
    return max_sum_subarray


def max_sum_subarray(arr):
    current_sum = arr[0]
    max_sum = arr[0]
    for element in arr[1:]:
        # if the single element is higher,the single element is a new sub array's starting
        current_sum = max(current_sum + element, element)
        # update the new max sum value
        max_sum = max(max_sum, current_sum)
    return max_sum


# Solution
'''
The Idea:
1. We have to find the sum of "contiguous" subarray, therefore we must not change the order of array elements.
2. Let `current_sum` denotes the sum of a subarray, and `max_sum` denotes the maximum value of `current_sum`.
3. LOOP STARTS: For each element of the array, update the `current_sum` with the MAXIMUM of either:
 - The element added to the `current_sum` (denotes the addition of the element to the current subarray)
 - The element itself  (denotes the starting of a new subarray)
 - Update (overwrite) `max_sum`, if it is lower than the updated `current_sum`
4. Return `max_sum`
'''


def max_sum_subarray_solution(arr):
    current_sum = arr[0]  # `current_sum` denotes the sum of a subarray
    max_sum = arr[0]  # `max_sum` denotes the maximum value of `current_sum` ever

    # Loop from VALUE at index position 1 till the end of the array
    for element in arr[1:]:
        '''
        # Compare (current_sum + element) vs (element)
        # If (current_sum + element) is higher, it denotes the addition of the element to the current subarray
        # If (element) alone is higher, it denotes the starting of a new subarray
        '''
        current_sum = max(current_sum + element, element)

        # Update (overwrite) `max_sum`, if it is lower than the updated `current_sum`
        max_sum = max(current_sum, max_sum)

    return max_sum


def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]

    output = max_sum_subarray(arr)
    if output == solution:
        print("Pass")
    else:
        print("Fail")


# arr = [1, 2, 3, -4, 6]
# solution = 8  # sum of array
#
# test_case = [arr, solution]
# test_function(test_case)

arr = [1, 2, -5, -4, 1, 6]
solution = 7  # sum of last two elements

test_case = [arr, solution]
test_function(test_case)

arr = [-12, 15, -13, 14, -1, 2, 1, -5, 4]
solution = 18  # sum of subarray = [15, -13, 14, -1, 2, 1]

test_case = [arr, solution]
test_function(test_case)
