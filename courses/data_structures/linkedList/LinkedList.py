from courses.data_structures.linkedList.Node import Node


class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next

    def __repr__(self):
        return str([v for v in self])
    # Solution

    # ----------------------------------------------------#


def prepend(self, value):
    """ Prepend a node to the beginning of the list """

    if self.head is None:
        self.head = Node(value)
        return

    new_head = Node(value)
    new_head.next = self.head
    self.head = new_head
    # ----------------------------------------------------#


def append(self, value):
    """ Append a node to the end of the list """
    # Here I'm not keeping track of the tail. It's possible to store the tail
    # as well as the head, which makes appending like this an O(1) operation.
    # Otherwise, it's an O(N) operation as you have to iterate through the
    # entire list to add a new tail.

    if self.head is None:
        self.head = Node(value)
        return

    node = self.head
    while node.next:
        node = node.next

    node.next = Node(value)
    # ----------------------------------------------------#


def search(self, value):
    """ Search the linked list for a node with the requested value and return the node. """
    if self.head is None:
        return None

    node = self.head
    while node:
        if node.value == value:
            return node
        node = node.next

    raise ValueError("Value not found in the list.")

    # ----------------------------------------------------#


def remove(self, value):
    """ Delete the first node with the desired data. """
    if self.head is None:
        return

    if self.head.value == value:
        self.head = self.head.next
        return

    node = self.head
    while node.next:
        if node.next.value == value:
            node.next = node.next.next
            return
        node = node.next

    raise ValueError("Value not found in the list.")

    # ----------------------------------------------------#


def pop(self):
    """ Return the first node's value and remove it from the list. """
    if self.head is None:
        return None

    node = self.head
    self.head = self.head.next

    return node.value
    # ----------------------------------------------------#


def insert(self, value, pos):
    """ Insert value at pos position in the list. If pos is larger than the
        length of the list, append to the end of the list. """
    # If the list is empty
    if self.head is None:
        self.head = Node(value)
        return

    if pos == 0:
        self.prepend(value)
        return

    index = 0
    node = self.head
    while node.next and index <= pos:
        if (pos - 1) == index:
            new_node = Node(value)
            new_node.next = node.next
            node.next = new_node
            return

        index += 1
        node = node.next
    else:
        self.append(value)

    # ----------------------------------------------------#


def size(self):
    """ Return the size or length of the linked list. """
    size = 0
    node = self.head
    while node:
        size += 1
        node = node.next

    return size
    # ----------------------------------------------------#


def to_list(self):
    out = []
    node = self.head
    while node:
        out.append(node.value)
        node = node.next
    return out


# Time complexity O(N)
def reverse(linked_list):
    """
    Reverse the inputted linked list

    Args:
       linked_list(obj): Linked List to be reversed
    Returns:
       obj: Reveresed Linked List
    """
    new_list = LinkedList()

    prev_node = None

    """
    A simple idea - Pick a node from the original linked list traversing form the beginning, and 
    prepend it to the new linked list. 
    We have to use a loop to iterate over the nodes of original linked list
    """
    # In this "for" loop, the "value" is just a variable whose value will be updated in each iteration
    for value in linked_list:
        # create a new node
        new_node = Node(value)

        # Make the new_node.next point to the
        # node created in previous iteration
        new_node.next = prev_node

        # This is the last statement of the loop
        # Mark the current new node as the "prev_node" for next iteration
        prev_node = new_node

    # Update the new_list.head to point to the final node that came out of the loop
    new_list.head = prev_node

    return new_list
