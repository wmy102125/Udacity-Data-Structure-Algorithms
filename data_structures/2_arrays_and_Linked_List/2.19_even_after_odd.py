"""
Problem Statement
Given a linked list with integer data, arrange the elements in such a manner that all nodes with even numbers are placed after odd numbers. Do not create any new nodes and avoid using any other data structure. The relative order of even and odd elements must not change.
Example:

linked list = 1 2 3 4 5 6
output = 1 3 5 2 4 6
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def even_after_odd(head):
    """
    :param - head - head of linked list
    return - updated list with all even elements are odd elements
    """
    if head is None:
        return
    odd_head = None
    odd_tail = None
    even_head = None
    even_tail = None
    while head:
        if head.data % 2 != 0:
            if odd_head is None:
                odd_head = head
                odd_tail = odd_head
            else:
                odd_tail.next = head
                odd_tail = odd_tail.next
        else:
            if even_head is None:
                even_head = head
                even_tail = even_head
            else:
                even_tail.next = head
                even_tail = even_tail.next

        head = head.next
    if odd_head is None:
        return even_head
    odd_tail.next = even_head
    return odd_head


"""
parameter: - head of the given linked list
return: - head of the updated list with all even elements placed after odd elements
"""
# --------------------------------------------------#
'''
The Idea: Traverse the given LinkedList, and build two sub-lists: EVEN and ODD. 
For this purpose, we will use four helper references, that denotes starting and 
current ending of EVEN and ODD sub-list respectively. 

1. For each Node in the LinkedList, check if its data is even/odd. 
Change the "next" reference (pointer) of each Node, based on the following rules:
 - First even valued Node will be referenced by head of EVEN sub-list
 - Subsequent even valued Node will be appended to the tail of EVEN sub-list

 - First odd valued Node will be referenced by head of ODD sub-list
 - Subsequent odd valued Node will be appended to the tail of ODD sub-list

2. After the loop, append the EVEN sub-list to the tail of ODD sub-list.
'''


# --------------------------------------------------#
def even_after_odd_solution(head):
    if head is None:
        return head

    # Helper references
    ''' `even_head` and `even_tail` represents the starting and current ending of the "EVEN" sub-list '''
    even_head = None
    even_tail = None

    ''' `odd_head` and `odd_tail` represents the starting and current ending of the "ODD" sub-list '''
    odd_head = None
    odd_tail = None

    current = head  # <-- "current" represents the current Node.

    # Loop untill there are Nodes available in the LinkedList
    while current:  # <-- "current" will be updated at the end of each iteration

        next_node = current.next  # <-- "next_node" represents the next Node w.r.t. the current Node

        if current.data % 2 == 0:  # <-- current Node is even

            # Below
            if even_head is None:  # <-- Make the current Node as the starting Node of EVEN sub-list
                even_head = current  # `even_head` will now point where `current` is already pointing
                even_tail = even_head
            else:  # <-- Append the current even node to the tail of EVEN sub-list
                even_tail.next = current
                even_tail = even_tail.next
        else:
            if odd_head is None:  # <-- Make the current Node as the starting Node of ODD sub-list
                odd_head = current
                odd_tail = odd_head
            else:  # <-- Append the current odd node to the tail of ODD sub-list
                odd_tail.next = current
                odd_tail = odd_tail.next
        current.next = None
        current = next_node  # <-- Update "head" Node, for next iteration

    if odd_head is None:  # <-- Special case, when there are no odd Nodes
        return even_head

    odd_tail.next = even_head  # <-- Append the EVEN sub-list to the tail of ODD sub-list

    return odd_head


# helper functions for testing purpose
def create_linked_list(arr):
    if len(arr) == 0:
        return None
    head = Node(arr[0])
    tail = head
    for data in arr[1:]:
        tail.next = Node(data)
        tail = tail.next
    return head


def print_linked_list(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()


def to_list(head):
    if head is None:
        return []
    else:
        node = head
        result = []
        while node:
            result.append(node.data)
            node = node.next
    return result


def test_function(test_case):
    head = test_case[0]
    solution = test_case[1]

    head = even_after_odd(head)
    sorted_list = to_list(head)
    if solution == sorted_list:
        print("Pass")
    else:
        print("Fail")


arr = [1, 2, 3, 4, 5, 6]
solution = [1, 3, 5, 2, 4, 6]

head = create_linked_list(arr)
test_case = [head, solution]
test_function(test_case)

arr = [1, 3, 5, 7]
solution = [1, 3, 5, 7]

head = create_linked_list(arr)
test_case = [head, solution]
test_function(test_case)

arr = [2, 4, 6, 8]
solution = [2, 4, 6, 8]
head = create_linked_list(arr)
test_case = [head, solution]
test_function(test_case)
