from exercise.Node import Node


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
