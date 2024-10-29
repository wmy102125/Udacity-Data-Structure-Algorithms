from unittest.mock import right

list1 = [0, 1, 2, 3]
midpoint1 = len(list1) // 2
print('List 1 midpoint: {}'.format(midpoint1))

list2 = [4, 5, 6]
midpoint2 = len(list2) // 2
print('List 2 midpoint: {}'.format(midpoint2))

left1 = list1[:midpoint1]
right1 = list1[midpoint1:]
print('List 1 left side: {}'.format(left1))
print('List 1 right side: {}'.format(right1))

left2 = list2[:midpoint2]
right2 = list2[midpoint2:]
print('List 2 left side: {}'.format(left2))
print('List 2 right side: {}'.format(right2))


def merge(left, right):
    merger_arry = []
    left_index = 0
    right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            merger_arry.append(right[right_index])
            right_index += 1
        else:
            merger_arry.append(left[left_index])
            left_index += 1
    merger_arry.extend(left[left_index:])
    merger_arry.extend(right[right_index:])
    return merger_arry


# Test this out
# merged = merge([1, 3, 7], [2, 5, 6])
# print(merged)
# merged = merge([3, 12, 7], [2, 15, 10])
# print(merged)


def merge_sort(data):
    if len(data) == 1:
        return data
    mid_index = len(data) // 2
    left = merge_sort(data[0:mid_index])
    right = merge_sort(data[mid_index:])
    return merge(left,right)

test_list_1 = [8, 3, 1, 7, 0, 10, 2]
test_list_2 = [1, 0]
test_list_3 = [97, 98, 99]
print('{} to {}'.format(test_list_1, merge_sort(test_list_1)))
print('{} to {}'.format(test_list_2, merge_sort(test_list_2)))
print('{} to {}'.format(test_list_3, merge_sort(test_list_3)))
