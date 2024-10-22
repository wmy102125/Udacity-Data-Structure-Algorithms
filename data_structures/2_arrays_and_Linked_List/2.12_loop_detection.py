""""
In computer science, linked lists are a fundamental data structure used to represent sequences of elements. However, linked lists can sometimes contain loops, where a node in the list points back to a previous node, creating a cycle. Detecting these loops is crucial for ensuring the integrity of operations on the list, as loops can lead to infinite loops in algorithms, memory leaks, and other unexpected behaviors.

Objective
In this exercise, you will implement a function to detect if a loop exists in a linked list. Detecting loops is a common problem with practical applications in various fields, such as network topology, graph theory, and debugging complex software systems.

The Two-Pointer Technique
To detect a loop, we'll use an efficient method known as the two-pointer or "runner" technique. This method involves two pointers that traverse the list at different speeds:

Slow Runner: This pointer moves one node per step.
Fast Runner: This pointer moves two nodes per step.
The key insight is that if there is a loop in the linked list, the fast runner will eventually lap the slow runner, causing both pointers to meet at the same node. Without a loop, the fast runner will reach the end of the list without ever meeting the slow runner.

Why Use the Two-Pointer Technique?
The two-pointer technique is efficient because it allows us to detect loops in linear time, O(n), and with constant space, O(1). This is significantly better than a naive approach, which might involve storing all visited nodes in a data structure and checking for repeats, which would require O(n) space.
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self, init_list=None):
        self.head = None
        if init_list:
            for value in init_list:
                self.append(value)

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


""""
Detecting Loops in Linked Lists
In this notebook, you'll implement a function that detects if a loop exists in a linked list. The way we'll do this is by having two pointers, called "runners", moving through the list at different rates. Typically we have a "slow" runner which moves at one node per step and a "fast" runner that moves at two nodes per step.

If a loop exists in the list, the fast runner will eventually move behind the slow runner as it moves to the beginning of the loop. Eventually it will catch up to the slow runner and both runners will be pointing to the same node at the same time. If this happens then you know there is a loop in the linked list. 
"""
def iscircular(linked_list):
    """
    Determine whether the Linked List is circular or not

    Args:
       linked_list(obj): Linked List to be checked
    Returns:
       bool: Return True if the linked list is circular, return False otherwise
    """
    slower = linked_list.head
    faster =  linked_list.head
    node = linked_list.head
    # TODO: Write function to check if linked list is circular
    while faster and faster.next:
        slower = slower.next
        faster = faster.next.next
        if slower == faster:
            return True
    return False


list_with_loop = LinkedList([2, -1, 3, 0, 5])

    # Creating a loop where the last node points back to the second node
loop_start = list_with_loop.head.next

node = list_with_loop.head
while node.next:
        node = node.next
node.next = loop_start
    # Test Cases

    # Create another circular linked list
small_loop = LinkedList([0])
small_loop.head.next = small_loop.head

print("Pass" if iscircular(list_with_loop) else "Fail")  # Pass
print("Pass" if iscircular(LinkedList([-4, 7, 2, 5, -1])) else "Fail")  # Fail
print("Pass" if iscircular(LinkedList([1])) else "Fail")  # Fail
print("Pass" if iscircular(small_loop) else "Fail")  # Pass
print("Pass" if iscircular(LinkedList([])) else "Fail")  # Fail
