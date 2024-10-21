# this code makes the tree that we'll traverse
"""
Breadth first search
Breadth first traversal of the tree would visit the nodes in this order:

tree image

apple, banana, cherry, dates

Think through the algorithm
We are walking down the tree one level at a time. So we start with apple at the root, and next are banana and cherry, and next is dates.

1) start at the root node
2) visit the root node's left child (banana), then right child (cherry)
3) visit the left and right children of (banana) and (cherry).

Queue
Notice that we're waiting until we visit "cherry" before visiting "dates". It's like they're waiting in line. We can use a queue to keep track of the order.

Python's collections module has a specialized deque datatype (ref: deque datatype documentation). We can append a new element to the right of the list with append method and to the left of the list with appendleft. To remove and return the right element of the list, we can use pop method.
"""
from collections import deque


class Node(object):

    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    # set value of the node
    def set_value(self, value):
        self.value = value

    # get value of the node
    def get_value(self):
        return self.value

    # set a node for the left child
    def set_left_child(self, left):
        self.left = left

    # set a node for the right child
    def set_right_child(self, right):
        self.right = right

    # get the node of left child
    def get_left_child(self):
        return self.left

    # get the node of right child
    def get_right_child(self):
        return self.right

    # check if node has left child -> return boolean
    def has_left_child(self):
        return self.left != None

    # check if node has right child -> return boolean
    def has_right_child(self):
        return self.right != None

    # define __repr_ to decide what a print statement displays for a Node object
    def __repr__(self):
        return f"Node({self.get_value()})"

    def __str__(self):
        return f"Node({self.get_value()})"


class Tree():
    def __init__(self, value=None):
        self.root = Node(value)

    def get_root(self):
        return self.root
    def __repr__(self):
        # visit order
        visit_order = list()
        # queue
        q = Queue()
        # start from the root
        node = self.get_root()
        # enque
        level = 0
        q.enq((node,level))
        # while queue is not Empty:
        while len(q) > 0 :
            # deq
            node,level = q.deq()
            # add deq into visit order
            # if node == None,add <empty> and level + 1,continue
            if node is None :
                visit_order.append(("<empty>",level))
                continue
            else:
                visit_order.append((node,level))
            # has_left_child: add left child and level+1
            if node.has_left_child():
                q.enq((node.get_left_child(),level + 1))
            # else : add None and level + 1
            else:
                q.enq((None,level + 1))
            # add right child and level + 1
            if node.has_right_child():
                q.enq((node.get_right_child(),level + 1))
            # else :add None and level + 1
            else :
                q.enq((None,level + 1))
        s = 'Tree \n'
        previous_level = -1
        # for i,node  visit order
        for i in range(len(visit_order)):
            node, level = visit_order[i]
            if level == previous_level:
                s += " | " + str(node)
            else:
                s += "\n" + str(node)
                previous_level = level

        return s



tree = Tree("apple")
tree.get_root().set_left_child(Node("banana"))
tree.get_root().set_right_child(Node("cherry"))
tree.get_root().get_left_child().set_left_child(Node("dates"))

"""Queue
Notice that we're waiting until we visit "cherry" before visiting "dates". It's like they're waiting in line. We can use a queue to keep track of the order.

Python's collections module has a specialized deque datatype (ref: deque datatype documentation). We can append a new element to the right of the list with append method and to the left of the list with appendleft. To remove and return the right element of the list, we can use pop method.
"""
class Queue():
    def __init__(self):
        self.q = deque()

    def enq(self, value):
        self.q.appendleft(value)

    def deq(self):
        if len(self.q) > 0:
            return self.q.pop()
        else:
            return None

    def __len__(self):
        return len(self.q)

    def __repr__(self):
        if len(self.q) > 0:
            s = "<enqueue here>\n_________________\n"
            s += "\n_________________\n".join([str(item) for item in self.q])
            s += "\n_________________\n<dequeue here>"
            return s
        else:
            return "<queue is empty>"
q = Queue()
q.enq("apple")
q.enq("banana")
q.enq("cherry")


visit_order = list()
q = Queue()

# start at the root node and add it to the queue
node = tree.get_root()
q.enq(node)
#print(q)

# dequeue the next node in the queue.
# "visit" that node
# also add its children to the queue

node = q.deq()
visit_order.append(node)
if node.has_left_child():
    q.enq(node.get_left_child())
if node.has_right_child():
    q.enq(node.get_right_child())

# print(f"visit order: {visit_order}")
# print(q)

# dequeue the next node (banana)
# visit it, and add its children (dates) to the queue

node = q.deq()
visit_order.append(node)
if node.has_left_child():
    q.enq(node.get_left_child())
if node.has_right_child():
    q.enq(node.get_right_child())

# print(f"visit order: {visit_order}")
# print(q)

# dequeue the next node (cherry)
# visit it, and add its children (there are None) to the queue

node = q.deq()
visit_order.append(node)
if node.has_left_child():
    q.enq(node.get_left_child())
if node.has_right_child():
    q.enq(node.get_right_child())

# print(f"visit order: {visit_order}")
# print(q)

# dequeue the next node (dates)
# visit it, and add its children (there are None) to the queue

node = q.deq()
visit_order.append(node)
if node.has_left_child():
    q.enq(node.get_left_child())
if node.has_right_child():
    q.enq(node.get_right_child())

# print(f"visit order: {visit_order}")
# print(q)

# BFS algorithm
def bfs(tree):
    # queue
    q = Queue()
    # visit order
    visit_order = list()
    # start at root
    node = tree.get_root()
    # enque
    q.enq(node)
    # while queue is not Empty:
    while len(q)>0:
        # deque the queue
        node = q.deq()
        # visit that code
        visit_order.append(node.get_value())
        # add left child  if exists
        if node.has_left_child():
            q.enq(node.get_left_child())
        # add right child if exists
        if node.has_right_child():
            q.enq(node.get_right_child())
    # return visit order
    return visit_order
#print(bfs(tree))
print(tree)

