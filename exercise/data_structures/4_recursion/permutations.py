# Code
"""
Permutation
Question - Let's use 4_recursion to help us solve the following permutation problem:

Given a list of items, the goal is to find all of the permutations of that list. For example,
Given a list like: [0, 1, 2]
Permutations: [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]]

Notice that the expected output is a list of permutation with each permuted item being represented by a list. Such an object that contains other object is called "compound" object.

The Idea
Build a compoundList incrementally starting with a blank list, and permute (add) each element of original input list at all possible positions.


For example, take [0, 1, 2] as the original input list:

Start with a blank compoundList [[]]. This is actually the last call of recursive function stack. Pick the element 2 of original input list, making the compoundList as [[2]]


Pick next element 1 of original input list, and add this element at position 0, and 1 for each list of previous compoundList. We will require to create copy of all lists of previous compoundList, and add the new element. Now, the compoundList will become [[1, 2], [2, 1]].


Pick next element 0 of original input list, and add this element at position 0, 1, and 2 for each list of previous compoundList. Now, the compoundList will become [[0, 1, 2], [1, 0, 2], [1, 2, 0], [0, 2, 1], [2, 0, 1], [2, 1, 0]] .
"""
import copy


def permute(inputList):
    """
    Args: myList: list of items to be permuted
    Returns: list of permutation with each permuted item being represented by a list
    """
    finalCompoundList = []
    if len(inputList) == 0 :
        finalCompoundList.append([])
        return finalCompoundList
    first_element = inputList[0]
    rest_elements = inputList[1:]
    sub_compund_list = permute(rest_elements)
    for sub_list in sub_compund_list:
        for i in range(len(sub_list)+1):
            inList = copy.deepcopy(sub_list)
            inList.insert(i,first_element)
            finalCompoundList.append(inList)
    return finalCompoundList
    pass


# Recursive Solution
"""
Args: myList: list of items to be permuted
Returns: compound list: list of permutation with each permuted item being represented by a list
"""
import copy  # We will use `deepcopy()` function from the `copy` module


def permute_solution(inputList):
    # a compound list
    finalCompoundList = []  # compoundList to be returned

    # Terminaiton / Base condition
    if len(inputList) == 0:
        finalCompoundList.append([])

    else:
        first_element = inputList[0]  # Pick one element to be permuted
        after_first = slice(1, None)  # `after_first` is an object of type 'slice' class
        rest_list = inputList[after_first]  # convert the `slice` object into a list

        # Recursive function call
        sub_compoundList = permute(rest_list)

        # Iterate through all lists of the compoundList returned from previous call
        for aList in sub_compoundList:

            # Permuted the `first_element` at all positions 0, 1, 2 ... len(aList) in each iteration
            for j in range(0, len(aList) + 1):
                # A normal copy/assignment will change aList[j] element
                bList = copy.deepcopy(aList)

                # A new list with size +1 as compared to aList
                # is created by inserting the `first_element` at position j in bList
                bList.insert(j, first_element)

                # Append the newly created list to the finalCompoundList
                finalCompoundList.append(bList)

    return finalCompoundList
# Test Cases

# Helper Function
def check_output(output, expected_output):
    """
    Return True if output and expected_output
    contains the same lists, False otherwise.

    Note that the ordering of the list is not important.

    Examples:
        check_output([ [0, 1], [1, 0] ] ], [ [1, 0], [0, 1] ]) returns True

    Args:
        output(list): list of list
        expected_output(list): list of list

    Returns:
        bool
    """
    o = copy.deepcopy(output)  # so that we don't mutate input
    e = copy.deepcopy(expected_output)  # so that we don't mutate input

    o.sort()
    e.sort()
    return o == e


print("Pass" if (check_output(permute([]), [[]])) else "Fail")
print(permute([0]))
print("Pass" if (check_output(permute([0]), [[0]])) else "Fail")
print("Pass" if (check_output(permute([0, 1]), [[0, 1], [1, 0]])) else "Fail")
print("Pass" if (
    check_output(permute([0, 1, 2]), [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]])) else "Fail")
