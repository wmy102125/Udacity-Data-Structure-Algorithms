# Here is our Stack Class

class Stack:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.size() == 0:
            return None
        else:
            return self.items.pop()


class Queue:
    def __init__(self):
        # Code here
        self.enqueue_stack = Stack()
        self.dequeue_stack = Stack()
        self.next_index = 0
        self.front_index = -1
        self.nums_element = 0

    def size(self):
        return self.nums_element

    # Code here

    def enqueue(self, item):
        self.enqueue_stack.push(item)
        self.nums_element += 1
        self.next_index = +1
        if self.nums_element == 0:
            self.front_index = 0

    # Code here

    def dequeue(self):
        # Code here
        if self.nums_element == 0:
            return None
        value = self.dequeue_stack.pop()
        if value is None:
            while not self.enqueue_stack.size() == 0 :
                self.dequeue_stack.push(self.enqueue_stack.pop())
            value = self.dequeue_stack.pop()
        self.front_index = self.front_index + 1
        self.nums_element -= 1
        return value


# Setup
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

# Test size
print ("Pass" if (q.size() == 3) else "Fail")

# Test dequeue
print ("Pass" if (q.dequeue() == 1) else "Fail")

# Test enqueue
q.enqueue(4)
print ("Pass" if (q.dequeue() == 2) else "Fail")
print ("Pass" if (q.dequeue() == 3) else "Fail")
print ("Pass" if (q.dequeue() == 4) else "Fail")
q.enqueue(5)
print ("Pass" if (q.size() == 1) else "Fail")