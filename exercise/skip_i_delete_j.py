# LinkedList Node class for your reference
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def skip_i_delete_j_mine(head, i, j):
    """
    :param: head - head of linked list
    :param: i - first `i` nodes that are to be skipped
    :param: j - next `j` nodes that are to be deleted
    return - return the updated head of the linked list
    linked-list = 1 2 3 4 5 6 7 8 9 10 11 12
    i = 2
    j = 3
    Output = 1 2 6 7 11 12
    """
    current = head
    retain_i = None
    delete_j = None
    if i ==0 :
        return None
    if j == 0 :
        return head
    while current:
        for index_i in range(i-1):
            retain_i = current
            if current:
                retain_i = retain_i.next
                current = current.next
        if current:
            for index_j in range(j):
                delete_j = current
                if delete_j.next:
                    delete_j = delete_j.next
                    current = delete_j
            retain_i.next = delete_j.next
        current = current.next


    return head

    pass


def skip_i_delete_j_mine_next(head, i, j):
    """
    :param: head - head of linked list
    :param: i - first `i` nodes that are to be skipped
    :param: j - next `j` nodes that are to be deleted
    return - return the updated head of the linked list
    linked-list = 1 2 3 4 5 6 7 8 9 10 11 12
    i = 2
    j = 3
    Output = 1 2 6 7 11 12
    """
    current = head
    retain_i = None
    delete_j = None
    if i ==0 :
        return None
    if j == 0 :
        return head
    if head is None or i < 0 or j<0:
        AssertionError("insert element error")
    while current:
        for index_i in range(i-1):
            if current is None:
                return head
            current = current.next
        retain_i = current
        current = current.next
        for index_j in range(j):
            if current is None:
                retain_i.next = current
                return head
            current = current.next
        retain_i.next = current


    return head

    pass


def skip_i_delete_j(head, i, j):
    # Edge case - Skip 0 nodes (means Delete all nodes)
    if i == 0:
        return None

    # Edge case - Delete 0 nodes
    if j == 0:
        return head

    # Invalid input
    if head is None or j < 0 or i < 0:
        return head

    # Helper references
    current = head
    previous = None

    # Traverse - Loop untill there are Nodes available in the LinkedList
    while current:

        '''skip (i - 1) nodes'''
        for _ in range(i - 1):
            if current is None:
                return head
            current = current.next
        previous = current
        current = current.next

        '''delete next j nodes'''
        for _ in range(j):
            if current is None:
                break
            next_node = current.next
            current = next_node

        '''Connect the `previous.next` to the `current`'''
        previous.next = current

    # Loop ends

    return head
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
    i = test_case[1]
    j = test_case[2]
    solution = test_case[3]

    temp = skip_i_delete_j(head, i, j)
    temp_list = to_list(temp)
    if solution == temp_list:
        print("Pass")
    else:
        print("Fail")


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
i = 2
j = 2
head = create_linked_list(arr)
solution = [1, 2, 5, 6, 9, 10]
test_case = [head, i, j, solution]
test_function(test_case)

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
i = 2
j = 3
head = create_linked_list(arr)
solution = [1, 2, 6, 7, 11, 12]
test_case = [head, i, j, solution]
test_function(test_case)

arr = [1, 2, 3, 4, 5]
i = 2
j = 4
head = create_linked_list(arr)
solution = [1, 2]
test_case = [head, i, j, solution]
test_function(test_case)

arr = [1, 2, 3, 4, 5]
i = 2
j = 0
head = create_linked_list(arr)
solution = [1, 2, 3, 4, 5]
test_case = [head, i, j, solution]
test_function(test_case)
