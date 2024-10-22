"""
In an encryption system where ASCII lower case letters represent numbers in the pattern a=1, b=2, c=3... and so on, find out all the codes that are possible for a given input number.

Example 1

number = 123
codes_possible = ["aw", "abc", "lc"]
Explanation: The codes are for the following number:

1 . 23 = "aw"
1 . 2 . 3 = "abc"
12 . 3 = "lc"
Example 2

number = 145
codes_possible = ["ade", "ne"]
Return the codes in a list. The order of codes in the list is not important.

Note: you can assume that the input number will not contain any 0s
"""


def all_codes_mine(number):
    """
    :param: number - input integer
    Return - list() of all codes possible for this number
    TODO: complete this method and return a list with all possible codes for the input number
    """
    if number == 0:
        return ['']
    result_list = list()

    first_digit = number % 10
    if 1 <= first_digit <= 9:
        sub_str = chr(first_digit + 96)
        num_str = number // 10
        for element in all_codes_mine(num_str):
            result_list.append(element + sub_str)
    first_two_digits = number % 100
    if 10 <= first_two_digits <= 26:
        sub_str = chr(first_two_digits + 96)
        num_str = number // 100
        for element in all_codes_mine(num_str):
            result_list.append(element + sub_str)
    return result_list


#print(all_codes_mine(1145))


# chatgtp
def decode(num_str):
    # 基本情况：空字符串返回空结果
    if not num_str:
        return [""]

    codes = []

    # 处理一位数
    first_digit = int(num_str[:1])
    if 1 <= first_digit <= 9:
        letter = chr(first_digit + ord('a') - 1)
        for code in decode(num_str[1:]):  # 递归处理剩余部分
            codes.append(letter + code)
            print("1", num_str, first_digit, letter, codes)

    # 处理两位数
    if len(num_str) > 1:
        first_two_digits = int(num_str[:2])
        if 10 <= first_two_digits <= 26:
            letter = chr(first_two_digits + ord('a') - 1)
            for code in decode(num_str[2:]):  # 递归处理剩余部分
                codes.append(letter + code)
                print("2", num_str, first_two_digits, letter, codes)

    return codes


print(decode("1145"))

# Solution

def get_alphabet(number):
    """
    Helper function to figure out alphabet of a particular number
    Remember:
        * ASCII for lower case 'a' = 97
        * chr(num) returns ASCII character for a number e.g. chr(65) ==> 'A'
    """
    return chr(number + 96)


def all_codes(number):
    if number == 0:
        return [""]

    # calculation for two right-most digits e.g. if number = 1123, this calculation is meant for 23
    remainder = number % 100
    output_100 = list()
    if 9 < remainder <= 26:

        # get all codes for the remaining number
        output_100 = all_codes(number // 100)
        alphabet = get_alphabet(remainder)

        for index, element in enumerate(output_100):
            output_100[index] = element + alphabet

    # calculation for right-most digit e.g. if number = 1123, this calculation is meant for 3
    remainder = number % 10

    # get all codes for the remaining number
    output_10 = all_codes(number // 10)
    alphabet = get_alphabet(remainder)

    for index, element in enumerate(output_10):
        output_10[index] = element + alphabet

    output = list()
    output.extend(output_100)
    output.extend(output_10)

    return output


def test_function(test_case):
    number = test_case[0]
    solution = test_case[1]

    output = all_codes(number)

    output.sort()
    solution.sort()

    if output == solution:
        print("Pass")
    else:
        print("Fail")

# number = 123
# solution = ['abc', 'aw', 'lc']
# test_case = [number, solution]
# test_function(test_case)
#
# number = 145
# solution = ['ade', 'ne']
# test_case = [number, solution]
# test_function(test_case)

# number = 1145
# solution = ['aade', 'ane', 'kde']
# test_case = [number, solution]
# test_function(test_case)

# number = 4545
# solution = ['dede']
# test_case = [number, solution]
# test_function(test_case)
