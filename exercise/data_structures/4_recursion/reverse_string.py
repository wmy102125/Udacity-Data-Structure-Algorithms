# Code
from numpy.matlib import empty


def reverse_string_mine(input):
    """
    Reverse a given string using 4_recursion.

    This function takes a string as input and returns a new string that is the reverse
    of the original. It uses a recursive approach to achieve this by repeatedly removing
    the first character from the string, reversing the rest, and then appending the
    first character to the reversed substring.

    Args:
        input (str): The string to be reversed.

    Returns:
        str: A new string that is the reverse of the input string.

    Example:
        >>> reverse_string("hello")
        'olleh'

    Details:
        - The function uses a base condition to terminate 4_recursion when the string is
          empty, returning an empty string.
        - It utilizes the `slice()` function to extract a substring starting from the
          second character.
        - The function recursively reverses the substring and concatenates the first
          character to the reversed result.
    """

    # TODO: Write your recursive string reverser solution here

    if len(input) == 0:
        return ""
    return input[len(input)-1] + reverse_string(input[0:len(input)-1])
    pass

def reverse_string(input):
    if len(input) == 0:
        return ""
    return reverse_string(input[slice(1,None)])+input[0]
# Solution
"""
RECURSIVE FUNCTION
Args: input(str): string to be reversed
Returns: a string that us reversed of input
"""


def reverse_string_solution(input):
    # (Recursion) Termination condition / Base condition
    if len(input) == 0:
        return ""

    else:
        first_char = input[0]

        '''
        The `slice()` function can accept upto the following three arguments.
        - start: [OPTIONAL] starting index. Default value is 0.
        - stop: ending index (exclusive)
        - step_size: [OPTIONAL] the increment size. Default value is 1.

        The return type of `slice()` function is an object of class 'slice'. 
        '''
        the_rest = slice(1, None)  # `the_rest` is an object of type 'slice' class
        sub_string = input[the_rest]  # convert the `slice` object into a list

        # Recursive call
        reversed_substring = reverse_string(sub_string)

        return reversed_substring + first_char


# -------------------------------------------------#
'''
**Time and Space Complexity Analysis**
Each recursive call to the `reverse_string()` function will create 
a new set of local variables - first_char, the_rest, sub_string, and reversed_substring. 
Therefore, the space complexity of a recursive function would always be proportional to the 
maximum depth of 4_recursion stack.  
The time complexity for this function will be  O(k*n), where k is a constant and n is the 
number of characters in the string (depth of 4_recursion stack). 
'''

# Test Cases

#print("Pass" if ("" == reverse_string("")) else "Fail")
print(reverse_string("abcs"))
print("Pass" if ("cba" == reverse_string("abc")) else "Fail")