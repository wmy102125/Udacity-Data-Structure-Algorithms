# this code makes the tree that we'll traverse
from collections import deque

class Node(object):

    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def set_left_child(self, left):
        self.left = left

    def set_right_child(self, right):
        self.right = right

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left != None

    def has_right_child(self):
        return self.right != None

    # define __repr_ to decide what a print statement displays for a Node object
    def __repr__(self):
        return f"Node({self.get_value()})"

    def __str__(self):
        return f"Node({self.get_value()})"


class Queue():
    def __init__(self):
        self.q = deque()

    def enq(self, value):
        self.q.appendleft(value)
    def deqLeft(self):
        if len(self.q) > 0:
            return self.q.popleft()
        else:
            return None
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


class Tree():
    def __init__(self):
        self.root = None

    def set_root(self, value):
        self.root = Node(value)

    def get_root(self):
        return self.root

    def compare_value(self, node_value, new_node_value):
        """
        0 means new_node equals node
        -1 means new node less than existing node
        1 means new node greater than existing node
        """
        if new_node_value == node_value:
            return 0
        elif new_node_value < node_value:
            return -1
        else:
            return 1
    def compare_node(node,new_node):
        if new_node.get_value() == node.get_value():
            return 0
        elif new_node.get_value() < node.get_value():
            return -1
        else:
            return 1
    def compare(self, node, new_node):
        """
        0 means new_node equals node
        -1 means new node less than existing node
        1 means new node greater than existing node
        """
        if new_node.get_value() == node.get_value():
            return 0
        elif new_node.get_value() < node.get_value():
            return -1
        else:
            return 1

    """
    define insert here
    can use a for loop (try one or both ways)
    """

    def insert_with_loop_mine(self, new_value):
        # ADD YOUR CODE HERE
        # start with root
        node = self.get_root()
        if node is None:
            self.set_root((new_value, 1))
            return
        node = self.get_root()
        # new_value < root:
        new_node = Node((new_value, 1))
        value, count = node.get_value()
        if new_value == value:
            if count is None: count = 0
            node.set_value((new_value, count + 1))
            return
        if new_value < value:
            # has_left_child :node = left_child
            while node is not None and node.has_left_child():
                node = node.get_left_child()
                value, count = node.get_value()
                if new_value > value:
                    node.set_right_child(new_node)
                    break
                if new_value == value:
                    value, count = node.get_value()
                    if count is None: count = 0
                    node.set_value((new_value, count + 1))
                    return
            node.set_left_child(new_node)

        # else:
        # has_right_child :node = right_child
        else:
            while node is not None and node.has_right_child():
                node = node.get_right_child()
                value, count = node.get_value()
                if new_value < value:
                    node.set_left_child(new_node)
                    break
                if new_value == value:
                    if count is None: count = 0
                    node.set_value((new_value, count + 1))
                    return
            node.set_right_child(new_node)

    """
    define insert here (can use 4_recursion)
    try one or both ways
    """

    def insert_with_recursion_mine(self, value):
        # ADD YOUR CODE HERE
        # start with root
        node = self.root
        # root is None:set root and return
        if node is None:
            self.set_root((value, 0))
            return

        # traverse()
        def traverse(node, value):
            e_value, count = node.get_value()
            if count is None: count = 0
            new_node = Node((value, count + 1))
            # root.value == value ,set root count+1
            if e_value == value:
                node.set_value((value, count + 1))
                return
            elif value < e_value and not node.has_left_child():
                node.set_left_child(new_node)
                return
            elif value > e_value and not node.has_right_child():
                node.set_right_child(new_node)
                return
            if value < e_value:
                if node.has_left_child():
                    traverse(node.get_left_child(), value)
            if value > e_value:
                if node.has_right_child():
                    traverse(node.get_right_child())

        traverse(node, value)
        return

    def insert_with_loop_value_count(self, value):
        node = self.get_root()
        if node is None:
            self.set_root((value, 1))
            return
        new_node = Node((value, 1))
        while (True):
            e_value, count = node.get_value()
            comparition = self.compare_value(e_value, value)
            if comparition == 0:
                if count is None:
                    count = 0
                node.set_value((value, count + 1))
                break
            if comparition == -1:
                if node.has_left_child():
                    node = node.get_left_child()
                else:
                    node.set_left_child(new_node)
                    break
            if comparition == 1:
                if node.has_right_child():
                    node = node.get_right_child()
                else:
                    node.set_right_child(new_node)
                    break

    def insert_with_recursion_value_count(self, value):
        node = self.get_root()
        if node is None:
            self.set_root((value, 1))
            return
        new_node = Node((value, 1))

        def traverse(node, new_node):
            e_value, count = node.get_value()
            comparition = self.compare_value(e_value, value)
            if comparition == 0:
                if count is None:
                    count = 0
                node.set_value((value, count + 1))
                return
            if comparition == -1:
                if node.has_left_child():
                    traverse(node.get_left_child(), new_node)
                else:
                    node.set_left_child(new_node)
                    return
            if comparition == 1:
                if node.has_right_child():
                    traverse(node.get_right_child(), new_node)
                else:
                    node.set_right_child(new_node)
                    return

        traverse(node, new_node)

    def insert_with_loop_solution(self, new_value):
        node = self.get_root()
        if node is None:
            self.set_root(new_value)
            return
        while (True):
            new_node = Node(new_value)
            comparition = self.compare(node, new_node)
            if comparition == 0:
                node.set_value(new_node)
                break
            if comparition == -1:
                if node.has_left_child():
                    node = node.get_left_child()
                else:
                    node.set_left_child(new_node)
                    break
            if comparition == 1:
                if node.has_right_child():
                    node = node.get_right_child()
                else:
                    node.set_right_child(new_node)
                    break
        return

    def insert_with_recursion_solution(self, new_value):
        node = self.get_root()
        if node is None:
            self.set_root(new_value)
            return

        def traverse(node, new_value):
            new_node = Node(new_value)
            comparition = self.compare(node, new_node)
            if comparition == 0:
                node.set_value(new_value)
                return
            if comparition == -1:
                if node.has_left_child():
                    traverse(node.get_left_child(), new_value)
                else:
                    node.set_left_child(new_node)
                    return
            if comparition == 1:
                if node.has_right_child():
                    traverse(node.get_right_child(), new_value)
                else:
                    node.set_right_child(new_node)
                    return

        traverse(node, new_value)

    def __repr__(self):
        level = 0
        q = Queue()
        visit_order = list()
        node = self.get_root()
        q.enq((node, level))
        while (len(q) > 0):
            node, level = q.deq()
            if node == None:
                visit_order.append(("<empty>", level))
                continue
            visit_order.append((node, level))
            if node.has_left_child():
                q.enq((node.get_left_child(), level + 1))
            else:
                q.enq((None, level + 1))

            if node.has_right_child():
                q.enq((node.get_right_child(), level + 1))
            else:
                q.enq((None, level + 1))

        s = "Tree\n"
        previous_level = -1
        for i in range(len(visit_order)):
            node, level = visit_order[i]
            if level == previous_level:
                s += " | " + str(node)
            else:
                s += "\n" + str(node)
                previous_level = level

        return s


# tree = Tree()
# tree.insert_with_loop_value_count(5)
# tree.insert_with_loop_value_count(6)
# tree.insert_with_loop_value_count(4)
# tree.insert_with_loop_value_count(2)
# tree.insert_with_loop_value_count(5)
# tree.insert_with_loop_value_count(6)
# tree.insert_with_loop_value_count(4)
# tree.insert_with_loop_value_count(4)
# print(tree)
#
# tree = Tree()
# tree.insert_with_recursion_value_count(5)
# tree.insert_with_recursion_value_count(6)
# tree.insert_with_recursion_value_count(4)
# tree.insert_with_recursion_value_count(2)
# tree.insert_with_recursion_value_count(6)
# tree.insert_with_recursion_value_count(6)
# tree.insert_with_recursion_value_count(4)
# tree.insert_with_recursion_value_count(2)
#
# print(tree)

# tree = Tree()
# tree.insert_with_recursion(5)
# tree.insert_with_recursion(6)
# tree.insert_with_recursion(4)
# tree.insert_with_recursion(2)
# tree.insert_with_recursion(5)  # insert duplicate
# print(tree)

    """Search
    Define a search function that takes a value, and returns true if a node containing that value exists in the tree, otherwise false."""
    """
    implement search
    """
    def search_mine(self, value):
            # ADD YOUR CODE HERE
            node = self.get_root()
            if node is None:
                return False

            def traverse(node, value):
                comparition = self.compare(node, Node(value))
                if comparition == 0:
                    return True
                if comparition == -1:
                    if node.has_left_child():
                        return traverse(node.get_left_child(), value)
                    else:
                        return False
                if comparition == 1:
                    if node.has_right_child():
                        return traverse(node.get_right_child(), value)
                    else:
                        return False

            return traverse(node, value)
    def search(self,value):
        node = self.get_root()
        if node is None:
            return False
        while(True):
            comparition = self.compare(node,Node(value))
            if comparition == 0:
                return True
            if comparition == -1:
                if node.has_left_child():
                    node = node.get_left_child()
                else:
                    return False
            if comparition == 1:
                if node.has_right_child():
                    node = node.get_right_child()
                else:
                    return False

# tree = Tree()
# tree.insert_with_loop_solution(5)
# tree.insert_with_loop_solution(6)
# tree.insert_with_loop_solution(4)
# tree.insert_with_loop_solution(2)
#
# print(f"""
# search for 8: {tree.search(8)}
# search for 2: {tree.search(2)}
# search for 2: {tree.search(5)}
# search for 2: {tree.search(4)}
# """)
# print(tree)
    """"
    delete solution at BST_delete.py"""
    def delete(self, value):
        node = self.get_root()
        if node is None:
            return
        Tree._delete(node, value)

    def _delete(node, value):
        comparition = Tree.compare_node(node, Node(value))
        # value < node.value ,traverse the left sub tree
        if comparition == -1:
            node.set_left_child(Tree._delete(node.get_left_child(), value))
        if comparition == 1:
            node.set_right_child(Tree._delete(node.get_right_child(), value))
        if comparition == 0:
            # it's the leaf
            if not node.has_left_child() and not node.has_right_child():
                return None
            # the node has one child
            if not node.has_left_child() and node.has_right_child():
                return node.get_right_child()
            if node.has_left_child() and not node.has_right_child():
                return node.get_left_child()
            if node.has_left_child() and node.has_right_child():
                # the node has two children，find the mix value at the right sub_tree which is bigger than value
                def find_mix_value(node, value):
                    if node.has_left_child():
                        return find_mix_value(node.get_left_child(), value)
                    return node

                mix_value_node = find_mix_value(node.get_right_child(), value)
                node.set_value(mix_value_node.get_value())
                node.set_right_child(Tree._delete(node.get_right_child(), mix_value_node.get_value()))
        return node



tree = Tree()
tree.insert_with_loop_solution(50)
tree.insert_with_loop_solution(30)
tree.insert_with_loop_solution(20)
tree.insert_with_loop_solution(40)
tree.insert_with_loop_solution(70)
tree.insert_with_loop_solution(60)
tree.insert_with_loop_solution(80)
tree.delete(50)
print(tree)
