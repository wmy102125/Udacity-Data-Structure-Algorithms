from exercise.Node import Node


class Stack:

    def __init__(self):
        self.head = None
        self.num_elements = 0

    def push(self, value):
        new_node = Node(value)
        # if 3_stacks_queues is empty
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head  # place the new node at the head (top) of the linked list
            self.head = new_node

        self.num_elements += 1

    # TODO: Add the pop method
    def pop(self):
        if self.head is None:
            self.num_elements = 0
            return
        value = self.head.value
        self.num_elements -= 1
        self.head = self.head.next
        return value

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0
# Setup
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)

# Test size
print ("Pass" if (stack.size() == 5) else "Fail")

# Test pop
print ("Pass" if (stack.pop() == 50) else "Fail")

# Test push
stack.push(60)
print ("Pass" if (stack.pop() == 60) else "Fail")
print ("Pass" if (stack.pop() == 40) else "Fail")
print ("Pass" if (stack.pop() == 30) else "Fail")
stack.push(50)
print ("Pass" if (stack.size() == 3) else "Fail")