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

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        # Move to the tail (the last node)
        node = self.head
        while node.next:
            node = node.next
        node.next = Node(value)
        return

    def to_list_wmy(self):
        # TODO: Write function to turn Linked List into Python List
        list = []
        if self.head is not None:
            head = self.head
            tail = head
            list.append(head.value)
            while tail.next:
                i = 0
                list.append(tail.next.value)
                i += 1
                tail = tail.next
        return list

    def to_list(self):
        list = []
        node = self.head
        while node:
            list.append(node.value)
            node = node.next
        return list

    # Test your method here
    # linked_list = LinkedList()
    # linked_list.append(3)
    # linked_list.append(2)
    # linked_list.append(-1)
    # linked_list.append(0.2)
    # # print("Pass" if (linked_list.to_list() == [3, 2, -1, 0.2]) else "Fail")
    # print("Pass" if (linked_list.to_list_better() == [3, 2, -1, 0.2]) else "Fail")

    # Define a function outside of the class
    def prepend(self, value):
        """ Prepend a value to the beginning of the list. """
        # TODO: Write function to prepend here
        prepend_node = Node(value)
        if self.head is None:
            self.head = prepend_node
            return
        prepend_node.next = self.head
        self.head = prepend_node
        return

    # Test prepend
    # linked_list = LinkedList()
    # linked_list.prepend(1)
    # assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"

    # Test append - 1
    # linked_list.append(3)
    # linked_list.prepend(2)
    # assert linked_list.to_list() == [2, 1, 3], f"list contents: {linked_list.to_list()}"
    #
    # # Test append - 2
    # linked_list = LinkedList()
    # linked_list.append(1)
    # assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"
    # linked_list.append(3)
    # assert linked_list.to_list() == [1, 3], f"list contents: {linked_list.to_list()}"
    def search(self, value):
        """ Search the linked list for a node with the requested value and return the node. """
        # TODO: Write function to search here
        if self.head is None:
            return None
        node = self.head
        while node:
            if node.value == value:
                return node
            node = node.next
        raise ValueError("Value not found in the list.")

    # Test search
    # linked_list = LinkedList()
    # linked_list.append(1)
    # linked_list.prepend(2)
    # linked_list.prepend(1)
    # linked_list.append(4)
    # linked_list.append(3)
    # print(linked_list.search(1))
    # print(linked_list.search(4))
    # assert linked_list.search(1).value == 1, f"list contents: {linked_list.to_list()}"
    # assert linked_list.search(4).value == 4, f"list contents: {linked_list.to_list()}"
    def remove_wmy(self, value):
        """ Remove first occurrence of value. """
        # TODO: Write function to remove here
        node = self.head
        pre_node = node
        while node:
            if node.value == value:
                if node == self.head:
                    self.head = node.next
                    return
                ## current node need to be removed
                ## previous node.next value need to be updated by current node.next
                ## head node is previous node now
                print(pre_node)
                pre_node.next = node.next
                node = self.head
                while node.value == pre_node.value:
                    node.next = pre_node.next
                    return
                return
            pre_node = node
            node = node.next
        return

    def remove(self, value):
        """ Remove first occurrence of value. """
        # TODO: Write function to remove here
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
        return

    # Test remove
    # linked_list = LinkedList()
    # linked_list.append(1)
    # linked_list.append(2)
    # linked_list.append(1)
    # linked_list.append(3)
    # linked_list.append(4)
    # linked_list.append(3)
    # #print(linked_list.to_list_better())
    # linked_list.remove(1)
    # #print(linked_list.to_list_better())
    # assert linked_list.to_list() == [2, 1, 3, 4, 3], f"list contents: {linked_list.to_list()}"
    # linked_list.remove(3)
    # print(linked_list.to_list_better())
    # assert linked_list.to_list() == [2, 1, 4, 3], f"list contents: {linked_list.to_list()}"
    # linked_list.remove(3)
    # print(linked_list.to_list_better())
    # assert linked_list.to_list() == [2, 1, 4], f"list contents: {linked_list.to_list()}"

    def pop(self):
        """ Return the first node's value and remove it from the list. """
        # TODO: Write function to pop here
        node = self.head
        if node is None:
            return
        self.head = self.head.next
        return node.value

    # Test pop
    # linked_list = LinkedList()
    # linked_list.append(2)
    # linked_list.append(1)
    # linked_list.append(3)
    # linked_list.append(4)
    # linked_list.append(3)
    # value = linked_list.pop()
    # assert value == 2, f"list contents: {linked_list.to_list()}"
    # assert linked_list.head.value == 1, f"list contents: {linked_list.to_list()}"
    def insert_wmy(self, value, pos):
        """ Insert value at pos position in the list. If pos is larger than the
        length of the list, append to the end of the list. """

        # TODO: Write function to insert here
        node = self.head
        # If pos is larger than the length of the list, append to the end of the list
        if pos == 0:
            self.prepend(value)
            return
        i = 0
        while node.next:
            i += 1
            node = node.next
        if pos > i:
            self.append(value)
            return
        # pos is shorter than the list's length
        else:
            j = 0
            node = self.head

            while node.next:
                if j + 1 == pos:
                    # insert position's previous node's next = value
                    # insert position's next node's next = node
                    origin_next_node = node.next
                    node.next = Node(value)
                    node.next.next = origin_next_node
                    return
                print(j)
                j += 1
                node = node.next
            return

    def insert(self, value, pos):
        """ Insert value at pos position in the list. If pos is larger than the
        length of the list, append to the end of the list. """

        # TODO: Write function to insert here
        if self.head is None:
            self.head = Node(value)
            return
        if pos == 0:
            self.prepend(value)
            return
        index = 0
        node = self.head
        while node.next and index <= pos:
            if index + 1 == pos:
                new_node = Node(value)
                new_node.next = node.next
                node.next = new_node
                return
            index += 1
            node = node.next
        else:
            self.append(value)
            return

    # Test insert
    # linked_list = LinkedList()
    # linked_list.append(1)
    # linked_list.append(4)
    # linked_list.insert(5, 0)
    # assert linked_list.to_list() == [5, 1, 4], f"list contents: {linked_list.to_list()}"
    # linked_list.insert(2, 1)
    # assert linked_list.to_list() == [5, 2, 1, 4], f"list contents: {linked_list.to_list()}"
    # linked_list.insert(3, 6)
    # assert linked_list.to_list() == [5, 2, 1, 4, 3], f"list contents: {linked_list.to_list()}"

    def size(self):
        """ Return the size or length of the linked list. """
        # TODO: Write function to get size here
        node = self.head
        size = 0
        while node:
            size += 1
            node = node.next
        return size

    # Test size function
    # linked_list = LinkedList()
    # linked_list.append(1)
    # linked_list.append(2)
    # linked_list.append(1)
    # linked_list.append(3)
    # linked_list.append(4)
    # assert linked_list.size() == 5, f"list contents: {linked_list.to_list()}"

    ##Test insert
    # linked_list = LinkedList()
    # linked_list.append(1)
    # linked_list.append(4)
    # linked_list.insert(5, 0)
    # assert linked_list.to_list() == [5, 1, 4], f"list contents: {linked_list.to_list()}"
    # linked_list.insert(2, 1)
    # assert linked_list.to_list() == [5, 2, 1, 4], f"list contents: {linked_list.to_list()}"
    # linked_list.insert(3, 6)
    # assert linked_list.to_list() == [5, 2, 1, 4, 3], f"list contents: {linked_list.to_list()}"

    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next

    def __repr__(self):
        return str([v for v in self])

"""Reversing a linked list exercise
Given a singly linked list, return another linked list that is the reverse of the first."""
def reverse_wmy(linked_list):
    """
    Reverse the inputted linked list

    Args:
       linked_list(obj): Linked List to be reversed
    Returns:
       obj: Reveresed Linked List
    """

    # TODO: Write your function to reverse linked lists here
    if linked_list.head is None:
        return
    array = [None] * linked_list.size()
    i = 0
    for item in linked_list:
        array[linked_list.size() - i - 1] = item
        i += 1
    new_linked_list = LinkedList()
    for item in array:
        new_linked_list.append(item)
    return new_linked_list

"""Reversing a linked list exercise
Given a singly linked list, return another linked list that is the reverse of the first."""
def reverse(linked_list):
    reverse_list = LinkedList()
    if linked_list.head is None:
        return None
    pre_node = None
    new_node= None
    for value in linked_list:
        new_node = Node(value)
        new_node.next = pre_node
        pre_node = new_node
    reverse_list.head = new_node
    return reverse_list


# llist = LinkedList()
# for value in [4, 2, 5, 1, -3, 0]:
#     llist.append(value)
#
# flipped = reverse(llist)
# is_correct = list(flipped) == list([0, -3, 1, 5, 2, 4]) and list(llist) == list(reverse(flipped))
# print("Pass" if is_correct else "Fail")

# Creating a loop where the last node points back to the second node

class DoubleNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        if self.head is None:
            self.head = DoubleNode(value)
            self.tail = self.head
            return
        else:
            self.tail.next = DoubleNode(value)
            self.tail.next.previous = self.tail
            self.tail = self.tail.next
    # Test your class here


linked_list = DoublyLinkedList()
linked_list.append(1)
linked_list.append(-2)
linked_list.append(4)

print("Going forward through the list, should print 1, -2, 4")
node = linked_list.head
while node:
    print(node.value)
    node = node.next

print("\nGoing backward through the list, should print 4, -2, 1")
node = linked_list.tail
while node:
    print(node.value)
    node = node.previous
