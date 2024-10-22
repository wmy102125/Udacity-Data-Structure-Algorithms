from tkinter.ttk import Label


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    def __repr__(self):
        return str(self.value)
    def __str__(self):
        if self.next is not None:
            return "Node\n value: %d \t next.value: %s " % (self.value, self.next.value)
        else:
            return "Node\n value: %d " % (self.value)

head = Node(2)
node2 = Node(1)
head.next = node2
# Add three more nodes to the list, with the values 4, 3, and 5
node3 = Node(4)
node2.next = node3
node4 = Node(3)
node3.next = node4
node5 = Node(5)
node4.next = node5


def print_nodes(head):
    current_node = head
    while current_node is not None:
        current_node = current_node.next


def create_linked_list(input_list):
    head = None
    for value in input_list:
        if head is None:
            head = Node(value)
        else:
            # Move to the tail (the last node)
            current_node = head
            while current_node.next:
                current_node = current_node.next
            current_node.next = Node(value)
    return head

### Test Code
def test_function(input_list, head):
    try:
        if len(input_list) == 0:
            if head is not None:
                print("Fail")
                return
        for value in input_list:
           # print(head.value)
            if head.value != value:
                print("Fail")
                return
            else:
                head = head.next
        print("Pass")
    except Exception as e:
        print("Fail: " + e)

# input_list = [1, 2, 3, 4, 5, 6]
# head = create_linked_list(input_list)
# test_function(input_list, head)

# input_list = [1]
# head = create_linked_list(input_list)
# test_function(input_list, head)
#
# input_list = []
# head = create_linked_list(input_list)
# test_function(input_list, head)

def create_linked_list_wmy(input_list):
    head = None
    current_node = None
    for value in input_list:
        if head is None:
            head = Node(value)
            current_node = head
        else:
            # Move to the tail (the last node)
            current_node.next = Node(value)
            current_node = current_node.next
    return head


def create_linked_list_better(input_list):
    head = None
    tail = None
    # TODO: Implement the more efficient version that keeps track of the tail
    for value in input_list:
        if head is None:
            head = Node(value)
            tail = head
        else:
            tail.next = Node(value)
            tail = tail.next
    return head



# input_list = [1, 2, 3, 4, 5, 6]
# head = create_linked_list_better(input_list)
# test_function(input_list, head)
# input_list = [1]
# head = create_linked_list_better(input_list)
# test_function(input_list, head)
#
# input_list = []
# head = create_linked_list_better(input_list)
# test_function(input_list, head)


