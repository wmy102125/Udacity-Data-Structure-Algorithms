from array import array


def count_inversions_mine(arry):
    array, count = count_inversions_merge(arry)
    return count


def count_inversions_merge(arr):
    # TODO: Complete this function
    if len(arr) == 1:
        return arr, 0
    mid_index = len(arr) // 2
    left, left_count = count_inversions_merge(arr[0:mid_index])
    right, right_count = count_inversions_merge(arr[mid_index:])
    merge, merge_count = _count_inversions(left, right)
    return merge, left_count + right_count + merge_count


def _count_inversions(left, right):
    inversion_ount = 0
    merger_arry = []
    left_index = 0
    right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            merger_arry.append(right[right_index])
            right_index += 1
            if left_index < right_index:
                inversion_ount += len(left) - left_index
        else:
            merger_arry.append(left[left_index])
            left_index += 1
    merger_arry.extend(left[left_index:])
    merger_arry.extend(right[right_index:])
    return merger_arry, inversion_ount


def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    if count_inversions_mine(arr) == solution:
        print("Pass")
    else:
        print("Fail")


arr = [2, 5, 1, 3, 4]
solution = 4
test_case = [arr, solution]
test_function(test_case)


def count_inversions(arr):
    start_index = 0
    end_index = len(arr) - 1
    output = inversion_count_func(arr, start_index, end_index)
    return output


def inversion_count_func(arr, start_index, end_index):
    if start_index >= end_index:
        return 0

    mid_index = start_index + (end_index - start_index) // 2

    # find number of inversions in left-half
    left_answer = inversion_count_func(arr, start_index, mid_index)

    # find number of inversions in right-half
    right_answer = inversion_count_func(arr, mid_index + 1, end_index)

    output = left_answer + right_answer

    # merge two sorted halves and count inversions while merging
    output += merge_two_sorted_halves(arr, start_index, mid_index, mid_index + 1, end_index)
    return output


def merge_two_sorted_halves(arr, start_one, end_one, start_two, end_two):
    count = 0
    left_index = start_one
    right_index = start_two

    output_length = (end_two - start_two + 1) + (end_one - start_one + 1)
    output_list = [0 for _ in range(output_length)]
    index = 0

    while index < output_length:
        # if left <= right, it's not an inversion
        if arr[left_index] <= arr[right_index]:
            output_list[index] = arr[left_index]
            left_index += 1

        else:
            count = count + (end_one - left_index + 1)  # left > right hence it's an inversion
            output_list[index] = arr[right_index]
            right_index += 1

        index = index + 1

        if left_index > end_one:
            for i in range(right_index, end_two + 1):
                output_list[index] = arr[i]
                index += 1
            break

        elif right_index > end_two:
            for i in range(left_index, end_one + 1):
                output_list[index] = arr[i]
                index += 1
            break

    index = start_one
    for i in range(output_length):
        arr[index] = output_list[i]
        index += 1
    return count
