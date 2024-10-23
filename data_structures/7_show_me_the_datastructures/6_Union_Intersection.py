from operator import truediv


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


def union(llist_1, llist_2):
    if llist_1 is None:
        llist2_set = convert_to_set(llist_2)
        return convert_to_linkedList(llist2_set)
    if llist_2 is None:
        llist1_set = convert_to_set(llist_1)
        return convert_to_linkedList(llist1_set)
    llist1_set = convert_to_set(llist_1)
    llist2_set = convert_to_set(llist_2)
    union_set = llist1_set | llist2_set
    return convert_to_linkedList(union_set)


def convert_to_set(llist):
    if llist is None:
        return None
    element_set = set()
    node = llist.head
    while node:
        element_set.add(node.value)
        node = node.next
    return element_set


def convert_to_linkedList(lset):
    if lset is None:
        return None
    union_list = LinkedList()
    head = union_list.head
    for element in lset:
        node = Node(element)
        if head is None:
            head = node
            union_list.head = head
        else:
            head.next = node
            head = head.next
    return union_list


def intersection(llist_1, llist_2):
    # Your Solution Here
    if llist_1 is None or llist_2 is None:
        return None
    llist1_set = convert_to_set(llist_1)
    llist2_set = convert_to_set(llist_2)
    intersection_set = llist1_set & llist2_set
    if len(intersection_set) == 0:
        return None
    return convert_to_linkedList(intersection_set)


## Add your own test cases: include at least three test cases
## and two of them must include edge cases, such as null, empty or very large values
def test_function(test_case):
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()
    element_1 = test_case[0]
    element_2 = test_case[1]
    if element_1 is not None:
        for i in element_1:
            linked_list_1.append(i)
    else:
        linked_list_1 = None

    if element_2 is not None:
        for i in element_2:
            linked_list_2.append(i)
    else:
        linked_list_2 = None
    output = union(linked_list_1, linked_list_2)
    if output is None:
        output_set = None
    else:
        output_set = sorted(convert_to_set(output))
    if output_set == test_case[2]:
        print("union Pass")
    else:
        print("union Fail")
    output = intersection(linked_list_1, linked_list_2)
    if output is None:
        output_set = None
    else:
        output_set = sorted(convert_to_set(output))
    if output_set == test_case[3]:
        print("insection Pass")
    else:
        print("insection Fail")


## Test Case 1

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
element_2 = [2, 3, 4]
union_result = [2, 3, 4, 6, 23, 35, 65]
insection_result = [2, 3, 4]
test_case_1 = [element_1, element_2, union_result, insection_result]
test_function(test_case_1)
## Test Case 2
element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
element_2 = [0, 7, 9]
union_result = [0, 2, 3, 4, 6, 7, 9, 23, 35, 65]
insection_result = None
test_case_2 = [element_1, element_2, union_result, insection_result]
test_function(test_case_2)
## Test Case 3
element_1 = None
element_2 = [0, 7, 9]
union_result = [0, 7, 9]
insection_result = None
test_case_3 = [element_1, element_2,union_result, insection_result]
test_function(test_case_3)

## Test Case 4
element_1 = None
element_2 = None
union_result = None
insection_result = None
test_case_4 = [element_1, element_2, union_result, insection_result]
test_function(test_case_4)
