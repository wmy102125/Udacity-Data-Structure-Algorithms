"""
Given a string consisting of uppercase and lowercase ASCII characters, write a function, case_sort, that sorts uppercase and lowercase letters separately, such that if the  𝑖
 th place in the original string had an uppercase character then it should not have a lowercase character after being sorted and vice versa.
"""


def case_sort(string):
    """
    Here are some pointers on how the function should work:
    1. Sort the string
    2. Create an empty output list
    3. Iterate over original string
        if the character is lower-case:
            pick lower-case character from sorted string to place in output list
        else:
            pick upper-case character from sorted string to place in output list

    Note: You can use Python's inbuilt ord() function to find the ASCII value of a character
    """
    output = ""
    sort_string = sorted(string)
    lower_string,upper_string = get_lower_upper_string(sort_string)
    for i, char in enumerate(string):
        # lower-case
        if ord(char) > 97:
            output += lower_string[0]
            lower_string = lower_string[1:]
        else:
            output += upper_string[0]
            upper_string = upper_string[1:]
    return str(output)


def get_lower_upper_string(string):
    for index, i in enumerate(string):
        if 97 <= ord(i) <= 122:
            return string[index:], string[0:index]


def case_sort_solution(string):
    upper_ch_index = 0
    lower_ch_index = 0

    sorted_string = sorted(string)
    for index, character in enumerate(sorted_string):
        # check if character is lower-case
        ascii_int = ord(character)
        if 97 <= ascii_int <= 122:  # ASCII value of a = 97 & ASCII value of z = 122
            lower_ch_index = index
            break

    output = list()
    for character in string:
        ascii_int = ord(character)
        # if character is lower case pick next lower_case character
        if 97 <= ascii_int <= 122:
            output.append(sorted_string[lower_ch_index])
            lower_ch_index += 1
        else:
            output.append(sorted_string[upper_ch_index])
            upper_ch_index += 1
    return "".join(output)


def test_function(test_case):
    test_string = test_case[0]
    solution = test_case[1]

    if case_sort(test_string) == solution:
        print("Pass")
    else:
        print("False")


print(ord("Z"))
test_string = 'fedRTSersUXJ'
solution = "deeJRSfrsTUX"
test_case = [test_string, solution]
test_function(test_case)

test_string = "defRTSersUXI"
solution = "deeIRSfrsTUX"
test_case = [test_string, solution]
test_function(test_case)
