"""
Problem 1: Square Root of an Integer
Finding the Square Root of an Integer
Find the square root of the integer without using any Python library. You have to find the floor value of the square root.

For example if the given number is 16, then the answer would be 4.

If the given number is 27, the answer would be 5 because √27=5.196, whose floor value is 5.

The expected time complexity is O(log(n))

Here is some boilerplate code and test cases to start with:
"""


def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number == 0 or number == 1:
        return number
    arr = [num for num in range(1, number // 2)]
    return _sqrt(arr, number, 0, len(arr) - 1)


def _sqrt(arr, number, start_index, end_index):
    if start_index >= end_index:
        return arr[start_index]
    mid_index = (start_index + end_index) // 2
    square_value = arr[mid_index] * arr[mid_index]
    if square_value == number:
        return arr[mid_index]
    elif square_value > number:
        # recursive the left sub_array
        return _sqrt(arr, number, start_index, mid_index - 1)
    elif square_value < number:
        # recursive the right sub_array
        return _sqrt(arr, number, mid_index + 1, end_index)


print("Pass" if 5 == sqrt(27) else "Fail")
print("Pass" if 3 == sqrt(9) else "Fail")
print("Pass" if 0 == sqrt(0) else "Fail")
print("Pass" if 4 == sqrt(16) else "Fail")
print("Pass" if 1 == sqrt(1) else "Fail")
