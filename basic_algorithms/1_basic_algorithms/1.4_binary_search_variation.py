"""
Variations on Binary Search
Now that you've gone through the work of building a binary search function, let's take some time to try out a few exercises that are variations (or extensions) of binary search. We'll provide the function for you to start:
"""
def recursive_binary_search(target, source, left=0):
    if len(source) == 0:
        return None
    center = (len(source) - 1) // 2
    if source[center] == target:
        return center + left
    elif source[center] < target:
        return recursive_binary_search(target, source[center + 1:], left + center + 1)
    else:
        return recursive_binary_search(target, source[:center], left)

"""
 Find First
The binary search function is guaranteed to return an index for the element you're looking for in an array, but what if the element appears more than once?

Consider this array:

[1, 3, 5, 7, 7, 7, 8, 11, 12]

Let's find the number 7:
 """

multiple = [1, 3, 5, 7, 7, 7, 8, 11, 12]
recursive_binary_search(7, multiple)


def find_first(target, source):
    index = recursive_binary_search(target, source)
    if index is None:
        return None

    while index > 0 and source[index - 1] == target:
        index -= 1
    return index


multiple = [1, 3, 5, 7, 7, 7, 8, 11, 12, 13, 14, 15]
print(find_first(7, multiple))  # Should return 3
print(find_first(9, multiple))  # Should return None

"""
Contains
The second variation is a function that returns a boolean value indicating whether an element is present, but with no information about the location of that element.

For example:

letters = ['a', 'c', 'd', 'f', 'g']
print(contains('a', letters)) ## True
print(contains('b', letters)) ## False
There are a few different ways to approach this, so try it out, and we'll share two solutions after.
"""
def contains(target, source):
    return recursive_binary_search(target, source)is not None

letters = ['a', 'c', 'd', 'f', 'g']
print(contains('a', letters)) ## True
print(contains('b', letters)) ## False

#Spoiler - Solution below:
#Here are two solutions we came up with:

#One option is just to wrap binary search:

def contains(target, source):
    return recursive_binary_search(target, source) is not None
#Another choice is to build a simpler binary search directly into the function:

def contains_recursion(target, source):
    # Since we don't need to keep track of the index, we can remove the `left` parameter.
    if len(source) == 0:
        return False
    center = (len(source) - 1) // 2
    if source[center] == target:
        return True
    elif source[center] < target:
        return contains(target, source[center + 1:])
    else:
        return contains(target, source[:center])