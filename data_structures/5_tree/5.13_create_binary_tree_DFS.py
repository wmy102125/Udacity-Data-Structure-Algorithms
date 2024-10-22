from numpy.f2py.crackfortran import traverse
""""
Depth First Search Intro
Traverse a tree (depth first search)
Traversing a tree means "visiting" all the nodes in the tree once. Unlike an array or linked list, there's more than one way to walk through a tree, starting from the root node.

Traversing a tree is helpful for printing out all the values stored in the tree, as well as searching for a value in a tree, inserting into or deleting values from the tree. There's depth first search and breadth first search.

Depth first search has 3 types: pre-order, in-order, and post-order.

Let's walk through pre-order traversal by hand first, and then try it out in code.
"""

class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def set_left_child(self, node):
        self.left = node

    def get_left_child(self):
        return self.left

    def set_right_child(self, node):
        self.right = node

    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left != None

    def has_right_child(self):
        return self.right != None

    def __repr__(self):
        return f"Node({self.get_value()})"

    def __str__(self):
        return f"Node({self.get_value()})"


class Tree(object):
    def __init__(self, value):
        self.root = Node(value)

    def get_root(self):
        return self.root


# Let's define a 3_stacks_queues to help keep track of the tree nodes
class Stack():
    def __init__(self):
        self.list = list()

    # add an element to the list
    def push(self, value):
        self.list.append(value)

    # remove the last element from the list
    def pop(self):
        return self.list.pop()

    # get the value of the last element in the list
    def top(self):
        if len(self.list) > 0:
            return self.list[-1]
        else:
            return None

    # check if the list empty
    def is_empty(self):
        return len(self.list) == 0

    #
    def __repr__(self):
        if len(self.list) > 0:
            s = "<top of 3_stacks_queues>\n_________________\n"
            s += "\n_________________\n".join([str(item) for item in self.list[::-1]])
            s += "\n_________________\n<bottom of 3_stacks_queues>"
            return s

        else:
            return "<3_stacks_queues is empty>"


class State(object):
    def __init__(self, node):
        self.node = node
        self.visited_left = False
        self.visited_right = False

    def get_node(self):
        return self.node

    def get_visited_left(self):
        return self.visited_left

    def get_visited_right(self):
        return self.visited_right

    def set_visited_left(self):
        self.visited_left = True

    def set_visited_right(self):
        self.visited_right = True

    def __repr__(self):
        s = f"""{self.node}
visited_left: {self.visited_left}
visited_right: {self.visited_right}
        """
        return s
#
tree = Tree("apple")
tree.get_root().set_left_child(Node("banana"))
tree.get_root().set_right_child(Node("cherry"))
# set second level's left child
# by getting the first level's left child first
tree.get_root().get_left_child().set_left_child(Node("dates"))


#
# # instantiate Stack
# 3_stacks_queues = Stack()
# # add elements into the 3_stacks_queues
# 3_stacks_queues.push("apple")
# 3_stacks_queues.push("banana")
# 3_stacks_queues.push("cherry")
# 3_stacks_queues.push("dates")
# # remove and print the last element (top of the 3_stacks_queues)
# print(3_stacks_queues.pop())
# print("\n")
# print(3_stacks_queues)
#
# visit_order = list()
# 3_stacks_queues = Stack()
#
# # start at the root node, visit it and then add it to the 3_stacks_queues
# node = tree.get_root()
# 3_stacks_queues.push(node)
#
# print(f"""
# visit_order {visit_order}
# 3_stacks_queues:
# {3_stacks_queues}
# """)
#
# # visit apple (root)
# visit_order.append(node.get_value())
# print(f"""visit order {visit_order}
# {3_stacks_queues}
# """)
#
# # check if apple (root) has a left child
# print(f"{node} has left child? {node.has_left_child()}")
#
# # since apple has a left child (banana)
# # we'll visit banana and add it to the 3_stacks_queues
# if node.has_left_child():
#     node = node.get_left_child()
#     3_stacks_queues.push(node)
#
# print(f"""
# visit_order {visit_order}
# 3_stacks_queues:
# {3_stacks_queues}
# """)
#
# # visit banana (first level's left child)
# print(f"visit {node}")
# visit_order.append(node.get_value())
# print(f"""visit_order {visit_order}""")
#
# # check if banana has a left child (second level's left chile)
# print(f"{node} has left child? {node.has_left_child()}")
#
# # since banana has a left child "dates"
# # we'll visit "dates" and add it to the 3_stacks_queues
# if node.has_left_child():
#     node = node.get_left_child()
#     3_stacks_queues.push(node)
#
# print(f"""
# visit_order {visit_order}
# 3_stacks_queues:
# {3_stacks_queues}
# """)
#
# # visit dates (second level's left chile)
# visit_order.append(node.get_value())
# print(f"visit order {visit_order}")
#
# # check if "dates" has a left child -> return boolean value
# print(f"{node} has left child? {node.has_left_child()}")
#
# # since dates doesn't have a left child, we'll check if it has a right child
# print(f"{node} has right child? {node.has_right_child()}")
#
# # since "dates" is a leaf node (has no children), we can start to retrace our steps
# # in other words, we can pop it off the 3_stacks_queues.
# print(3_stacks_queues.pop())
#
# print(3_stacks_queues)
#
# # now we'll set the node to the new top of the 3_stacks_queues, which is banana
# node = 3_stacks_queues.top()
# print(node)
#
# # we already checked for banana's left child, so we'll check for its right child
# print(f"{node} has right child? {node.has_right_child()}")
#
# # banana doesn't have a right child, so we're also done tracking it.
# # so we can pop banana off the 3_stacks_queues
# print(f"pop {3_stacks_queues.pop()} off 3_stacks_queues")
# print(f"""
# 3_stacks_queues
# {3_stacks_queues}
# """)
#
# # now we'll track the new top of the 3_stacks_queues, which is apple
# node = 3_stacks_queues.top()
# print(node)
#
# # we've already checked if apple has a left child; we'll check if it has a right child
# print(f"{node} has right child? {node.has_right_child()}")
#
# # since it has a right child (cherry),
# # we'll visit cherry and add it to the 3_stacks_queues.
# if node.has_right_child():
#     node = node.get_right_child()
#     3_stacks_queues.push(node)
#
# print(f"""
# visit_order {visit_order}
# 3_stacks_queues
# {3_stacks_queues}
# """)
#
# # visit cherry (first level's right child)
# print(f"visit {node}")
# visit_order.append(node.get_value())
# print(f"""visit_order: {visit_order}""")
#
# # Now we'll check if cherry (first level's right child) has a left child
# print(f"{node} has left child? {node.has_left_child()}")
#
# # it doesn't, so we'll check if it has a right child
# print(f"{node} has right child? {node.has_right_child()}")
#
# # since cherry has neither left nor right child nodes,
# # we are done tracking it, and can pop it off the 3_stacks_queues
#
# print(f"pop {3_stacks_queues.pop()} off the 3_stacks_queues")
#
# print(f"""
# visit_order {visit_order}
# 3_stacks_queues
# {3_stacks_queues}
# """)
#
# # now we're back to apple at the top of the 3_stacks_queues.
# # since we've already checked apple's left and right child nodes,
# # we can pop apple off the 3_stacks_queues
#
# print(f"pop {3_stacks_queues.pop()} off 3_stacks_queues")
# print(f"pre-order traversal visited nodes in this order: {visit_order}")
#
# print(f"""3_stacks_queues
# {3_stacks_queues}""")

""""
Depth first, pre-order traversal with a 3_stacks_queues
pre-order traversal of the tree would visit the nodes in this order:

tree image

apple, banana, dates, cherry
"""
def pre_order_with_stack(tree, debug_mode=False):
    visit_order = list()
    stack = Stack()
    node = tree.get_root()
    visit_order.append(node.get_value())
    state = State(node)
    stack.push(state)
    count = 0
    while (node):
        if debug_mode:
            print(f"""
loop count: {count}
current node: {node}
3_stacks_queues:
{stack}
            """)
        count += 1
        if node.has_left_child() and not state.get_visited_left():
            state.set_visited_left()
            node = node.get_left_child()
            visit_order.append(node.get_value())
            state = State(node)
            stack.push(state)

        elif node.has_right_child() and not state.get_visited_right():
            state.set_visited_right()
            node = node.get_right_child()
            visit_order.append(node.get_value())
            state = State(node)

        else:
            stack.pop()
            if not stack.is_empty():
                state = stack.top()
                node = state.get_node()
            else:
                node = None

    if debug_mode:
        print(f"""
loop count: {count}
current node: {node}
3_stacks_queues:
{stack}
            """)
    return visit_order



#pre_order_with_stack(tree, debug_mode=True)

def pre_order(tree):
    node = tree.get_root()
    visit_order = list()
    def traverse(node):
        if node:
            # visit
            visit_order.append(node.get_value())
            # visit the left child
            traverse(node.get_left_child())
            # visit the right child
            traverse(node.get_right_child())
    traverse(node)
    return visit_order
print(pre_order(tree))

"""Task: do in-order traversal¶
We want to traverse the left subtree, then visit the node, and then traverse the right subtree.

hint: it's very similar in structure to the pre-order traversal."""
# define in-order traversal
def in_order(tree):
    node = tree.get_root()
    visit_order = list()
    def traverse(node):
        if node:
            # visit the left child
            traverse(node.get_left_child())
            # visit
            visit_order.append(node.get_value())
            # visit the right child
            traverse(node.get_right_child())
    traverse(node)
    return visit_order
# check solution: should get: ['dates', 'banana', 'apple', 'cherry']
print(in_order(tree))

"""Task: post-order traversal
Traverse left subtree, then right subtree, and then visit the node."""

# define post_order traversal
def post_order(tree):
    node = tree.get_root()
    visit_order = list()

    def traverse(node):
        if node:
            # visit the left child
            traverse(node.get_left_child())
            # visit the right child
            traverse(node.get_right_child())
            # visit
            visit_order.append(node.get_value())
    traverse(node)
    return visit_order
# check solution: should get: ['dates', 'banana', 'cherry', 'apple']
print(post_order(tree))