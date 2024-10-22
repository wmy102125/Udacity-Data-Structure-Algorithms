"""
Create a sorted linked list
Given a stream of random integers, create a linked list that is always sorted from ascending order (lowest to highest). What's the computational complexity of adding an element in this way?
"""
# Use this class as the nodes in your linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class SortedLinkedList:
    def __init__(self):
        self.head = None

    def append_wmy(self, value):
        """
        Append a value to the Linked List in ascending sorted order

        Args:
           value(int): Value to add to Linked List
        """

        # TODO: Write your sorted append function here
        if self.head is None:
            self.head = Node(value)
            return
        node = self.head
        if self.head.value > value:
            self.head = Node(value)
            self.head.next = node
            return

        while node.next:
            origin_next_node = node.next
            if node.next.value > value:
                node.next = Node(value)
                node.next.next = origin_next_node
                return
            node = node.next
        pass

    def append(self, value):
        """
        Append a value to the Linked List in ascending sorted order

        Args:
           value(int): Value to add to Linked List
        """

        # TODO: Write your sorted append function here
        if self.head is None:
            self.head = Node(value)
            return
        node = self.head
        if self.head.value > value:
            self.head = Node(value)
            self.head.next = node
            return

        while node.next is not None and node.next.value < value:
            node = node.next
        origin_next_node = node.next
        node.next = Node(value)
        node.next.next = origin_next_node
        pass

    '''We will need this function to convert a LinkedList object into a Python list of integers'''

    def to_list(self):
        out = []  # <-- Declare a Python list
        node = self.head  # <-- Create a temporary Node object

        while node:  # <-- Iterate untill we have nodes available
            out.append(int(str(
                node.value)))  # <-- node.value is actually of type Node, therefore convert it into int before appending to the Python list
            node = node.next

        return out


    def sort(array):
        """
        Given an array of integers, use SortedLinkedList to sort them and return a sorted array.

        Args:
           array(array): Array of integers to be sorted
        Returns:
           array: Return sorted array
        """

        # TODO: Write your sorting function here

        if array is None or len(array) == 0 :
            return None
        sorted_list = SortedLinkedList()
        if len(array) == 1:
            sorted_list.append(array[0])
        else:
            for arr in array:
                sorted_list.append(arr)
        new_array = []
        node = sorted_list.head
        while node:
            new_array.append(node.value)
            node = node.next
        return new_array
        pass
# Test cases
linked_list = SortedLinkedList()
linked_list.append(5)
print("Pass" if (linked_list.to_list() == [5]) else "Fail")

linked_list.append(3)
print("Pass" if (linked_list.to_list() == [3, 5]) else "Fail")

linked_list.append(4)
print("Pass" if (linked_list.to_list() == [3, 4, 5]) else "Fail")

# Test case
print ("Pass" if (SortedLinkedList.sort([4, 8, 2, 1, -3, 1, 5]) == [-3, 1, 1, 2, 4, 5, 8]) else "Fail")