"""Problem Statement
Given an input string, return all permutations of the string in an array.

Example 1:

string = 'ab'
output = ['ab', 'ba']
Example 2:

string = 'abc'
output = ['abc', 'bac', 'bca', 'acb', 'cab', 'cba']
Note - Strings are Immutable
Strings in Python are immutable, whch means that we cannot overwrite the characters of the String objects. For example:

str1 = "Hello"
str1[0] = 'K'                         # Try changing the first character
will lead to

TypeError: 'str' object does not support item assignment
We can only re-assign the variable to a new value (string), as follows:

str1 = "Udacity"                      # re-assignment
str2 = "Welcome to the " + str1[3:]   # Returns 'Welcome to the city'
Therefore, we do not require a deep copy in this exercise, as it was the case in our last example of list permutation.

The Idea
Starting with a blank list, add each character of original input string at all possible positions.


For example, take "abc" as the original string:

Start with a blank list() object. This is actually the last call of recursive function 3_stacks_queues. Pick a character 'c' of original string, making the output as ['c']


Pick next character b of original input string, and place the current character at different indices of the each sub-string of previous output. We can make use of the sub-string of previous output, to create a new sub-string. Now, the output will become ['bc', 'cb'].


Pick next character a of original input string, and place the current character at different indices of the each sub-string of previous output. Now, the output will become ['abc', 'bac', 'bca', 'acb', 'cab', 'cba']"""
import copy


def permutations(string):
    """
    :param: input string
    Return - list of all permutations of the input string
    TODO: complete this function to return a list of all permutations of the string
    """
    permute_list = []
    if len(string)== 0:
        permute_list.append('')
        return permute_list
    first_str = string[0]
    rest_strs = string[1:]
    sub_permute_list = permutations(rest_strs)
    for sub_list in sub_permute_list:
        for i in range(len(sub_list)+1):
            in_list = sub_list[0:i] + first_str +sub_list[i:]
            permute_list.append(in_list)
    return permute_list

    pass


def test_function(test_case):
        string = test_case[0]
        solution = test_case[1]
        output = permutations(string)

        output.sort()
        solution.sort()

        if output == solution:
            print("Pass")
        else:
            print("Fail")
string = 'ab'
solution = ['ab', 'ba']
test_case = [string, solution]
test_function(test_case)

string = 'abc'
output = ['abc', 'bac', 'bca', 'acb', 'cab', 'cba']
test_case = [string, output]
test_function(test_case)

string = 'abcd'
output = ['abcd', 'bacd', 'bcad', 'bcda', 'acbd', 'cabd', 'cbad', 'cbda', 'acdb', 'cadb', 'cdab', 'cdba', 'abdc', 'badc', 'bdac', 'bdca', 'adbc', 'dabc', 'dbac', 'dbca', 'adcb', 'dacb', 'dcab', 'dcba']
test_case = [string, output]
test_function(test_case)