

def sort_a_little_bit(items, left_index, pivot_index):
    if left_index >= pivot_index:
        return pivot_index
    while pivot_index != left_index:
        pivot_value = items[pivot_index]
        if pivot_value < items[left_index]:
            items[pivot_index] = items[left_index]
            items[left_index] = items[pivot_index - 1]
            items[pivot_index - 1] = pivot_value
            pivot_index -= 1
        else:
            left_index += 1


# items = [8, 3, 1, 7, 0, 10, 2]
# pivot_index = sort_a_little_bit(items, 0, len(items) - 1)
# print(items)
# print('pivot index %d' % pivot_index)

def sort_all(items, left_index, pivot_index):
    if pivot_index <= left_index:
        return
    sort_a_little_bit(items, left_index, pivot_index)
    ## sort right sublist
    sort_all(items, pivot_index + 1, len(items) - 1)
    ## sort left sublist
    sort_all(items, left_index, pivot_index - 1)
    return items


def quicksort(items):
    return sort_all(items, 0, len(items) - 1)



items = [8, 3, 1, 7, 0, 10, 2]
print(quicksort(items))
