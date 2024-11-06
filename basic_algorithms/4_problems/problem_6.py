"""
Problem 6: Unsorted Integer Array
Max and Min in a Unsorted Array
In this problem, we will look for smallest and largest integer from a list of unsorted integers. The code should run inO(n) time. Do not use Python's inbuilt functions to find min and max.

Bonus Challenge: Is it possible to find the max and min in a single traversal?
"""

def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    min_value = ints[0]
    max_value = ints[0]
    for index,value in enumerate(ints):
        if value < min_value:
            min_value = value
        if value > max_value :
            max_value = value
    return min_value,max_value

### Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)
print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

l = [i for i in range(1000, 2000)]  # a list containing 0 - 9
random.shuffle(l)
print("Pass" if ((1000, 1999) == get_min_max(l)) else "Fail")

l = [i for i in range(28, 100)]  # a list containing 0 - 9
random.shuffle(l)
print("Pass" if ((28, 99) == get_min_max(l)) else "Fail")