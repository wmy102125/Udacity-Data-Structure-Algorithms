# User defined class
from exercise.Node import Node


class FlatternLinkedList:
    def __init__(self, head):  # <-- Expects "head" to be a Node made up of an int or LinkedList
        self.head = head

    '''
    For creating a simple LinkedList, we will pass an integer as the "value" argument
    For creating a nested LinkedList, we will pass a LinkedList as the "value" argument
    '''

    def append(self, value):

        # If LinkedList is empty
        if self.head is None:
            self.head = Node(value)
            return

        # Create a temporary Node object
        node = self.head

        # Iterate till the end of the currrent LinkedList
        while node.next is not None:
            node = node.next

        # Append the newly creataed Node at the end of the currrent LinkedList
        node.next = Node(value)

    '''We will need this function to convert a LinkedList object into a Python list of integers'''

    def flattern_to_list(self):
        out = []  # <-- Declare a Python list
        node = self.head  # <-- Create a temporary Node object

        while node:  # <-- Iterate untill we have nodes available
            out.append(int(str(node.value)))  # <-- node.value is actually of type Node, therefore convert it into int before appending to the Python list
            node = node.next

        return out


    def merge(list1, list2):
        # TODO: Implement this function so that it merges the two linked lists in a single, sorted linked list.
        '''
        The arguments list1, list2 must be of type LinkedList.
        The merge() function must return an instance of LinkedList.
        '''
        merge = FlatternLinkedList(None)
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        list1_elt = list1.head
        list2_elt = list2.head
        while list1_elt is not None or list2_elt is not None:
            print("merge loop")
            if list1_elt is None:
                merge.append(list2_elt.value)
                list2_elt = list2_elt.next
                continue
            if list2_elt is None:
                merge.append(list1_elt.value)
                list1_elt = list1_elt.next
                continue
            if list1_elt.value <= list2_elt.value:
                merge.append(list1_elt.value)
                list1_elt = list1_elt.next
                continue
            if list1_elt.value > list2_elt.value:
                merge.append(list2_elt.value)
                list2_elt = list2_elt.next
                continue

        return merge
''' In a NESTED LinkedList object, each node will be a simple LinkedList in itself'''
class NestedLinkedList(FlatternLinkedList):
    # [[1,3,5],[2,4]]
    def flatten(self):
    ## TODO: Implement this method to flatten the linked list in ascending sorted order.
        return self._flatten(self.head)
    def _flatten(self,node):
        if node.next is None:
           print("node.next is None")
           return FlatternLinkedList.merge(node.value,None)
        print("node.next is not None")
        return FlatternLinkedList.merge(node.value,self._flatten(node.next))
    def while_flatten(self):
        ## while can not solve this problem
        node = self.head
        flattened = FlatternLinkedList(Node(None))
        while node :
            if node.next is None:
                flattened.append(FlatternLinkedList.merge(node.value,None))
                break;
            flattened.append(FlatternLinkedList.merge(node.value,node.next.value))
            node = node.next
        return flattened
# ''' Test merge() function'''
# linked_list = FlatternLinkedList(Node(1))
# linked_list.append(3)
# linked_list.append(5)
#
# second_linked_list = FlatternLinkedList(Node(2))
# second_linked_list.append(4)
#
# merged = FlatternLinkedList.merge(linked_list, second_linked_list)
# node = merged.head
# while node is not None:
#  # This will print 1 2 3 4 5
#    # print(node)
#     print(node.value)
#     node = node.next
#
#     # Lets make sure it works with a None list
# merged = FlatternLinkedList.merge(None, linked_list)
# node = merged.head
# while node is not None:
#         # This will print 1 3 5
#     #print(node.value)
#     node = node.next



# First Test scenario
''' Create a simple LinkedList'''
linked_list = FlatternLinkedList(Node(1)) # <-- Notice that we are passing a Node made up of an integer
linked_list.append(3) # <-- Notice that we are passing a numerical value as an argument in the append() function here
linked_list.append(5)

''' Create another simple LinkedList'''
second_linked_list = FlatternLinkedList(Node(2))
second_linked_list.append(4)
''' Test flatten() function'''
# Create a nested linked list with one node.
# The node itself is a simple linked list as 1-->3-->5 created previously
nested_linked_list = NestedLinkedList(Node(linked_list))

# Append a node (a linked list as 2-->4) to the existing nested linked list
nested_linked_list.append(second_linked_list)
node = nested_linked_list.head
while node:
    item = node.value.head
    while item:
        item = item.next
    node = node.next

# solution = nested_linked_list.flatten() # <-- returns A LinkedList object
#
# expected_list = [1,2,3,4,5] # <-- Python list
#
# # Convert the "solution" into a Python list and compare with another Python list
# assert solution.flattern_to_list() == expected_list, f"list contents: {solution.flattern_to_list()}"
# Call the `flatten()` function
third_linked_list = FlatternLinkedList(Node(6))
third_linked_list.append(7)
nested_linked_list.append(third_linked_list)
flattened = nested_linked_list.flatten()

# Logic to print the flattened list
node = flattened.head
while node is not None:
    #This will print 1 2 3 4 5
    print(node.value)
    node = node.next

#
# while_flattened = nested_linked_list.while_flatten()
# while_node = while_flattened.head
# while while_node :
#     print("------",while_node.value)
#     while_node = while_node.next