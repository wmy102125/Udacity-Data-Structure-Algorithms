# For this exercise we will be using an Adjacency List representation to store the graph.

# Class Node representation.
class Node:
    def __init__(self, val):
        self.value = val
        self.children = []

    def add_child(self, new_node):
        self.children.append(new_node)

    def remove_child(self, del_node):
        if del_node in self.children:
            self.children.remove(del_node)


class Graph():
    def __init__(self, node_list):
        self.nodes = node_list

    def add_edge(self, node1, node2):
        if (node1 in self.nodes and node2 in self.nodes):
            node1.add_child(node2)
            node2.add_child(node1)

    def remove_edge(self, node1, node2):
        if (node1 in self.nodes and node2 in self.nodes):
            node1.remove_child(node2)
            node2.remove_child(node1)


# Creating a graph as above.
nodeG = Node('G')
nodeR = Node('R')
nodeA = Node('A')
nodeP = Node('P')
nodeH = Node('H')
nodeS = Node('S')

graph1 = Graph([nodeS, nodeH, nodeG, nodeP, nodeR, nodeA])

graph1.add_edge(nodeG, nodeR)
graph1.add_edge(nodeA, nodeR)
graph1.add_edge(nodeA, nodeG)
graph1.add_edge(nodeR, nodeP)
graph1.add_edge(nodeH, nodeG)
graph1.add_edge(nodeH, nodeP)
graph1.add_edge(nodeS, nodeR)

# To verify that the graph is created accurately.
# Let's just print all the parent nodes and child nodes.
# for each in graph1.nodes:
#     print('parent node = ', each.value, end='\nchildren\n')
#     for each in each.children:
#         print(each.value, end=' ')
#     print('\n')

'''TO DO'''


def dfs_recursion_start(start_node, search_value):
    visited = [start_node]
    return _dfs_recursion_start(start_node, search_value, visited)


def _dfs_recursion_start(node, search_value, visited):
    if node.value == search_value:
        return node
    for current_node in node.children:
        if current_node.value == search_value:
            return current_node
        if current_node not in visited:
            visited.append(current_node)
            #if the lopp is ended but not come in this condition,this function will be ended,so we need
            # return the None
            # return _dfs_recursion_start(current_node, search_value, visited)
            result = _dfs_recursion_start(current_node, search_value, visited)
            if result is not None:
                return result
    return None


# solution
def dfs_recursion_start_solution(start_node, search_value):
    visited = set()  # Set to keep track of visited nodes
    return dfs_recursion(start_node, visited, search_value)

# Recursive function
def dfs_recursion(node, visited, search_value):
    if node.value == search_value:
        return node  # Return node if search value is found

    visited.add(node)
    for child in node.children:
        if child not in visited:
            result = dfs_recursion(child, visited, search_value)
            if result is not None:
                return result  # Return the result immediately if found
    return None  # Return None if the value is not found in any of the paths

assert nodeA == dfs_recursion_start(nodeG, 'A')
assert nodeA == dfs_recursion_start(nodeS, 'A')
assert nodeS == dfs_recursion_start(nodeP, 'S')
assert nodeR == dfs_recursion_start(nodeH, 'R')
