"""Problem statement
Given an input_list and a target, return the pair of indices in the list that holds the values which sum to the target. For example,

input_list = [1, 5, 9, 7] and target = 8, the answer would be [0, 3]

Note

The best solution takes O(n) time. This means that you cannot traverse the given list more than once. Hint - Think of an additional data structure that you should use here.
You can assume that the list does not have any duplicates."""


def pair_sum_to_target(input_list, target):
    index_dicts = dict()
    for index, element in enumerate(input_list):
        if (target - element) in index_dicts:
            return [index_dicts[target - element], index]
        index_dicts[element] = index


# complex is O(n^2)
def pair_sum_to_target_mine(input_list, target):
    output = [0]

    # TODO: Write pair sum to target function
    def _pair_sum_to_target(start, input_list, target):
        if start < target and (target - start) in input_list[output[0]:]:
            for i in range(len(input_list)):
                if (target - start) == input_list[i]:
                    output.append(i)
                    return output
        # if the target is 0 -4 = -4
        if start == 0 and target in input_list[1:]:
            for i in range(len(input_list)):
                if target == input_list[i]:
                    output.append(i)
                    return output
        output[0] += 1
        _pair_sum_to_target(input_list[1:], target)

    return _pair_sum_to_target(input_list[0], input_list, target)


def test_function(test_case):
    output = pair_sum_to_target(test_case[0], test_case[1])
    print(output)
    if sorted(output) == test_case[2]:
        print("Pass")
    else:
        print("Fail")


test_case_1 = [[1, 5, 9, 7], 8, [0, 3]]
test_function(test_case_1)

test_case_3 = [[0, 1, 2, 3, -4], -4, [0, 4]]
test_function(test_case_3)
