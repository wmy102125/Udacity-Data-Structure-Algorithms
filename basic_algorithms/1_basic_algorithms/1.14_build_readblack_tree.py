class Node(object):
    def __init__(self, value, parent, color):
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent
        self.color = color


class RedBlackTree(object):
    def __init__(self, root):
        self.root = Node(root, None, 'red')

    def insert(self, new_val):
        node = self.insert_recursion(self.root, new_val)
        self.rebalance(node)

    def insert_recursion(self, current_node, new_val):
        if current_node.value < new_val:
            if current_node.right:
                return self.insert_recursion(current_node.right, new_val)
            else:
                current_node.right = Node(new_val, current_node, 'red')
                return current_node.right
        if current_node.value > new_val:
            if current_node.left:
                return self.insert_recursion(current_node.left, new_val)
            else:
                current_node.left = Node(new_val, current_node, 'red')
                return current_node.left

    # def search(self, find_val):
    #     return False

    def grandparent(self, node):
        if node is None:
            return
        return node.node.parent

    def pibling(self, node):
        p = self.grandparent(node)
        if p.left == node:
            return p.right
        if p.right == node:
            return p.left

    def rebalance(self, node):
        # case 1 node.parent is None,current node is the root
        if node.parent is None:
            return
        # case 2 node.parent's color is black
        if node.parent.color == 'black':
            return
        # from here all below the parent's color is red
        # case 3 the  parent's  color is red and the node's pibling color is red,node,parent,pibling are both red
        gp = self.grandparent(node)
        pibling = self.pibling(node)
        if pibling.color == 'red':
            node.parent.color = 'black'
            pibling.color = 'black'
            if gp.color == 'black':
                return
            else:
                self.rebalance(gp)
        # parent is red ,but pibling is black
        # case 4 the newly insert node is on the insider of the subtree,rotate the subtree to an outer subtree
        if gp.left and gp.left.right == node:
            self.rotate_left(node.parent)
        elif gp.right and gp.right.left == node:
            self.rotate_right(node.parent)
        # case 5 the newly insert node is on the outsider of the subtree,rotate the subtree
        if gp.left and gp.left.left == node:
            self.rotate_right(node.parent.parent)
        elif gp.right and gp.right.right == node:
            self.rotate_left(node.parent.parent)
        node.parent.color = 'black'
        node.parent.parent.color = 'red'

    def rotate_left(self, node):
        parent = node.parent
        move_up_node = node.right
        node.right = move_up_node.left
        move_up_node.left = node
        node.parent = move_up_node
        if parent is not None:
            if parent.left == node:
                parent.left = move_up_node
            if parent.right == node:
                parent.right = move_up_node
        move_up_node.parent = parent

    def rotate_right(self, node):
        parent = node.parent
        move_up_node = node.left
        node.left = move_up_node.right
        move_up_node.right = node
        node.parent = move_up_node
        if parent is not None:
            if parent.left == node:
                parent.left = move_up_node
            if parent.right == node:
                parent.right = move_up_node
        move_up_node.parent = parent
