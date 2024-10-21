from array import array


def duplicate_number(arr):
    """
    :param - array containing numbers in the range [0, len(arr) - 2]
    return - the number that is duplicate in the arr
    """
    if arr is None or len(arr) == 0:
        return
    sum_list = []
    for i in range(len(arr)):
        if arr[i] > len(arr) - 2:
            raise ValueError('%s is out of the range [0,%s]' % arr[i], len(arr) - 2)
        if arr[i] in sum_list:
            return arr[i]
        sum_list.append(arr[i])
    pass


def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    output = duplicate_number(arr)
    if output == solution:
        print("Pass")
    else:
        print("Fail")


arr = [0, 0]
solution = 0

test_case = [arr, solution]
test_function(test_case)

arr = [0, 2, 3, 1, 4, 5, 3]
solution = 3

test_case = [arr, solution]
test_function(test_case)

arr = [0, 1, 5, 5, 3, 2, 4]
solution = 5

test_case = [arr, solution]
test_function(test_case)
