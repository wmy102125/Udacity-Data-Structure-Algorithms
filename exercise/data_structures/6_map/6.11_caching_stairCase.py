"""A child is running up a staircase and can hop either 1 step, 2 steps or 3 steps at a time. Given that the staircase has a total n steps, write a function to count the number of possible ways in which child can run up the stairs.

For e.g.

n == 1 then answer = 1

n == 3 then answer = 4
The output is 4 because there are four ways we can climb the staircase:

1 step + 1 step + 1 step
1 step + 2 steps
2 steps + 1 step
3 steps
n == 5 then answer = 13

Hint
You would need to make use of the Inductive Hypothesis, which comprises of the following two steps:

The Inductive Hypothesis: Calculate/assume the results for base case. In our problem scenario, the base cases would be when n = 1, 2, and 3.
The Inductive Step: Prove that for every  𝑛>=3
 , if the results are true for  𝑛
  , then it holds for  (𝑛+1)
  as well. In other words, assume that the statement holds for some arbitrary natural number  𝑛
  , and prove that the statement holds for  (𝑛+1)
 ."""


# 4_recursion
def staircase_traverse(n):
    print(n)
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    return staircase_traverse(n - 1) + staircase_traverse(n - 2) + staircase_traverse(n - 3)


def staircase_mine(n):
    num_dicts = dict({})
    return _staircase_mine(n, num_dicts)


def _staircase_mine(n, num_dicts):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    else:
        if (n - 1) in num_dicts:
            first_value = num_dicts[n - 1]
        else:
            first_value = _staircase_mine(n - 1, num_dicts)
        if (n - 2) in num_dicts:
            second_value = num_dicts[n - 2]
        else:
            second_value = _staircase_mine(n - 2, num_dicts)
        if (n - 3) in num_dicts:
            third_value = num_dicts[n - 3]
        else:
            third_value = _staircase_mine(n - 3, num_dicts)
        output = first_value + second_value + third_value
        num_dicts[n] = output
        return output


def staircase(n):
    num_dict = dict({})
    return staircase_faster(n, num_dict)


def staircase_faster(n, num_dict):
    if n == 1:
        output = 1
    elif n == 2:
        output = 2
    elif n == 3:
        output = 4
    else:
        if (n - 1) in num_dict:
            first_output = num_dict[n - 1]
        else:
            first_output = staircase_faster(n - 1, num_dict)

        if (n - 2) in num_dict:
            second_output = num_dict[n - 2]
        else:
            second_output = staircase_faster(n - 2, num_dict)

        if (n - 3) in num_dict:
            third_output = num_dict[n - 3]
        else:
            third_output = staircase_faster(n - 3, num_dict)

        output = first_output + second_output + third_output

    num_dict[n] = output;
    return output


def test_function(test_case):
    answer = staircase(test_case[0])
    if answer == test_case[1]:
        print("Pass")
    else:
        print("Fail")


test_case = [5, 13]
test_function(test_case)

num_dict = dict({})
num_dict[0] = 1
print(num_dict)
