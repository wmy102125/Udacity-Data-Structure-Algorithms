# second try
class Heap:
    def __init__(self, initial_size):
        self.cbt = [None for _ in range(initial_size)]  # initialize arrays
        self.next_index = 0  # denotes next index where new element should go

    def _up_heapity(self, data):
        if self.next_index == 0 or self.next_index == 1:
            return
        current_index = self.next_index - 1
        return self._up_heapity_recursion(data, current_index)

    def _up_heapity_recursion(self, data, current_index):
        parent_index = (current_index - 1) // 2
        if self.cbt[parent_index] > data:
            self.cbt[current_index] = self.cbt[parent_index]
            self.cbt[parent_index] = data
            return self._up_heapity_recursion( data, parent_index)
        else:
            return

    def insert(self, data):
        """
        Insert `data` into the heap
        """
        self.cbt[self.next_index] = data
        self.next_index += 1
        self._up_heapity(data)
        # if out of array capacity
        if self.next_index > len(self.cbt):
            old_array = self.cbt
            self.cbt = [None for _ in range(len(self.cbt) * 2)]
            for index in range(len(old_array)):
                self.cbt[index] = old_array[index]

    def size(self):
        return self.next_index

    def _down_heapify(self):
        return self._down_heapify_recursion(0)

    def _down_heapify_recursion(self, parent_index):
        data = self.cbt
        left_child_index = 2 * parent_index + 1
        right_child_index = 2 * parent_index + 2
        if left_child_index > self.size() or right_child_index > self.size():
            return
        min_value = min(data[parent_index], data[left_child_index], data[right_child_index])
        if min_value == data[parent_index]:
            return
        elif data[left_child_index] is not None and min_value == data[left_child_index]:
            self.cbt[left_child_index] = self.cbt[parent_index]
            self.cbt[parent_index] = min_value
            return self._down_heapify_recursion(left_child_index)
        elif data[right_child_index] is not None and min_value == data[right_child_index]:
            self.cbt[right_child_index] = self.cbt[parent_index]
            self.cbt[parent_index] = min_value
            return self._down_heapify_recursion(right_child_index)

    def remove(self):
        """
        Remove and return the element at the top of the heap
        """
        if self.size() == 0:
            return
        if self.size() == 1:
            self.next_index = 0
            self.cbt[0] = None
            return
        self.cbt[0] = self.cbt[self.next_index - 1]
        self.cbt[self.next_index - 1] = None
        old_next_index = self.next_index
        self.next_index = old_next_index - 1
        self._down_heapify()
heap_size = 6
heap = Heap(heap_size)

elements = [1, 2, 3, 4, 1, 2]
# for element in elements:
#     heap.insert(element)
# print('Inserted elements: {}'.format(elements))
for element in elements:
    heap.insert(element)

print('Inserted elements: {}'.format(elements))
print('Inserted elements: {}'.format(heap.cbt))
heap.remove()
print('final elements: {}'.format(heap.cbt))