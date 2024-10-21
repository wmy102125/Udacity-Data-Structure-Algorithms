# You are provided with basic implementations of a Queue class and a Stack class.
# Your task is to write a function called reverse_queue
# that takes a queue as input and reverses the order of its elements.
# The function should modify the original queue in place without returning any value.
class LinkedListNode:

    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:

    def __init__(self):
        self.num_elements = 0
        self.head = None

    def push(self, data):
        new_node = LinkedListNode(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.num_elements += 1

    def pop(self):
        if self.is_empty():
            return None
        temp = self.head.data
        self.head = self.head.next
        self.num_elements -= 1
        return temp

    def top(self):
        if self.head is None:
            return None
        return self.head.data

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0


class Queue:

    def __init__(self):
        self.head = None
        self.tail = None
        self.num_elements = 0

    def enqueue(self, data):
        new_node = LinkedListNode(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.num_elements += 1

    def dequeue(self):
        if self.is_empty():
            return None
        temp = self.head.data
        self.head = self.head.next
        self.num_elements -= 1
        return temp

    def front(self):
        if self.head is None:
            return None
        return self.head.data

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0

    def reverse_queue_mine(queue):
        """
        Reverse the order of elements in a queue.

        Args:
            queue (Queue): An instance of the Queue class.

        Returns:
            None: The function modifies the input queue in place and does not return a value.
        """

        # TODO: Write reversed queue function
        if queue is None or queue.size() == 0:
            return
        holder_queue = Queue()
        while not queue.size() == 0:
            holder_queue.enqueue(queue.dequeue())
        Queue._reverse_queue(queue,holder_queue)
        pass

    def _reverse_queue(queue, holder_queue):
        if holder_queue.size() == 0:
            return
        value = holder_queue.dequeue()
        Queue._reverse_queue(queue, holder_queue)
        queue.enqueue(value)

    def reverse_queue(queue):
        stack = Stack()
        while not queue.is_empty():
            stack.push(queue.dequeue())
        while not stack.is_empty():
            queue.enqueue(stack.pop())

    def reverse_queue_solution(queue):
        stack = Stack()
        while not queue.is_empty():
            stack.push(queue.dequeue())

        while not stack.is_empty():
            queue.enqueue(stack.pop())

    def test_function(test_case):
        queue = Queue()
        for num in test_case:
            queue.enqueue(num)

        Queue.reverse_queue(queue)
        index = len(test_case) - 1
        while not queue.is_empty():
            removed = queue.dequeue()
            if removed != test_case[index]:
                print("Fail")
                return
            else:
                index -= 1
        print("Pass")
test_case_1 = [1, 2, 3, 4]
Queue.test_function(test_case_1)
test_case_2 = [1]
Queue.test_function(test_case_2)
