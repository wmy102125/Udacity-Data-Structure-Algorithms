from collections import defaultdict


class Graph:
    def __init__(self):
        # {'A', 'B', 'C', 'D', 'E'}
        self.nodes = set()  # A set cannot contain duplicate nodes
        # defaultdict(<class 'list'>, {'A': ['B', 'D'], 'B': ['A', 'D', 'E', 'C'], 'D': ['A', 'B', 'E'], 'E': ['B', 'C', 'D'], 'C': ['B', 'E']})
        self.neighbours = defaultdict(
            list)  # Defaultdict is a child class of Dictionary that provides a default value for a key that does not exists.
        # {('A', 'B'): 3, ('A', 'D'): 2, ('B', 'A'): 3, ('B', 'C'): 1, ('B', 'D'): 4, ('B', 'E'): 6, ('C', 'B'): 1, ('C', 'E'): 2, ('D', 'A'): 2, ('D', 'B'): 4, ('D', 'E'): 1, ('E', 'B'): 6, ('E', 'C'): 2, ('E', 'D'): 1}
        self.distances = {}  # Dictionary. An example record as ('A', 'B'): 6 shows the distance between 'A' to 'B' is 6 units

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.neighbours[from_node].append(to_node)
        self.neighbours[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance
        self.distances[(to_node, from_node)] = distance  # lets make the 2_graph undirected / bidirectional

    def print_graph(self):
        print("Set of Nodes are: ", self.nodes)
        print("Neighbours are: ", self.neighbours)
        print("Distances are: ", self.distances)


''' TO DO: Find the shortest path from the source node to every other node in the given 2_graph '''


def dijkstra(graph, source):
    # Declare and initialize result, unvisited, and path
    result = dict()

    for i in graph.nodes:
        if i == source:
            result[source] = 0
        else:
            result[i] = sys.maxsize
    unvisited = graph.nodes
    path = dict()
    # As long as unvisited is non-empty
    while unvisited:

        # 1. Find the unvisited node having smallest known distance from the source node.
        min_node = None
        for node in unvisited:
            if min_node is None:
                min_node = node
            if result[node] < result[min_node]:
                min_node = node
        # 2. For the current node, find all the unvisited neighbours. For this, you have calculate the distance of each unvisited neighbour.
        # neighbours:{'A': ['B', 'D'], 'B': ['A', 'D', 'E', 'C'], 'D': ['A', 'B', 'E'], 'E': ['B', 'C', 'D'], 'C': ['B', 'E']})
        # distances:{('A', 'B'): 3, ('A', 'D'): 2, ('B', 'A'): 3, ('B', 'C'): 1, ('B', 'D'): 4, ('B', 'E'): 6, ('C', 'B'): 1, ('C', 'E'): 2, ('D', 'A'): 2, ('D', 'B'): 4, ('D', 'E'): 1, ('E', 'B'): 6, ('E', 'C'): 2, ('E', 'D'): 1}
        for current_node in graph.neighbours[min_node]:
            # distance_A = 0,distance_A-B:distance_A+distance_(A,B)
            distance = result[min_node] + graph.distances[min_node, current_node]
            # 3. If the calculated distance of the unvisited neighbour is less than the already known distance in result dictionary, update the shortest distance in the result dictionary.
            if distance < result[current_node]:
                result[current_node] = distance
            # 4. If there is an update in the result dictionary, you need to update the path dictionary as well for the same key.
            path[current_node] = min_node
        # 5. Remove the current node from the unvisited set.
        unvisited.remove(min_node)

    return result


import sys

# solution
'''Find the shortest path from the source node to every other node in the given 2_graph'''


def dijkstra_solution(graph, source):
    result = {}
    result[source] = 0

    for node in graph.nodes:
        if (node != source):
            result[node] = sys.maxsize

    unvisited = set(graph.nodes)

    path = {}

    '''THE GREEDY APPROACH'''
    # As long as unvisited is non-empty
    while unvisited:
        min_node = None

        # 1. Find the unvisited node having smallest known distance from the source node.
        for node in unvisited:
            if node in result:

                if min_node is None:
                    min_node = node
                elif result[node] < result[min_node]:
                    min_node = node

        if min_node is None:
            break

        # known distance of min_node
        current_distance = result[min_node]

        # 2. For the current node, find all the unvisited neighbours.
        # For this, you have calculate the distance of each unvisited neighbour.
        for neighbour in graph.neighbours[min_node]:
            if neighbour in unvisited:
                distance = current_distance + graph.distances[(min_node, neighbour)]

                # 3. If the calculated distance of the unvisited neighbour is less than the already known distance in result dictionary, update the shortest distance in the result dictionary.
                if ((neighbour not in result) or (distance < result[neighbour])):
                    result[neighbour] = distance

                    # 4. If there is an update in the result dictionary, you need to update the path dictionary as well for the same key.
                    path[neighbour] = min_node

        # 5. Remove the current node from the unvisited set.
        unvisited.remove(min_node)

    return result


# Test 1
testGraph = Graph()
for node in ['A', 'B', 'C', 'D', 'E']:
    testGraph.add_node(node)

testGraph.add_edge('A', 'B', 3)
testGraph.add_edge('A', 'D', 2)
testGraph.add_edge('B', 'D', 4)
testGraph.add_edge('B', 'E', 6)
testGraph.add_edge('B', 'C', 1)
testGraph.add_edge('C', 'E', 2)
testGraph.add_edge('E', 'D', 1)

# print(dijkstra(testGraph, 'A'))  # {'A': 0, 'D': 2, 'B': 3, 'E': 3, 'C': 4}

# Test 2
graph = Graph()
for node in ['A', 'B', 'C']:
    graph.add_node(node)

graph.add_edge('A', 'B', 5)
graph.add_edge('B', 'C', 5)
graph.add_edge('A', 'C', 10)

# print(dijkstra(2_graph, 'A'))  # {'A': 0, 'C': 10, 'B': 5}

# Test 3
graph = Graph()
for node in ['A', 'B', 'C', 'D', 'E', 'F']:
    graph.add_node(node)

graph.add_edge('A', 'B', 5)
graph.add_edge('A', 'C', 4)
graph.add_edge('D', 'C', 1)
graph.add_edge('B', 'C', 2)
graph.add_edge('A', 'D', 2)
graph.add_edge('B', 'F', 2)
graph.add_edge('C', 'F', 3)
graph.add_edge('E', 'F', 2)
graph.add_edge('C', 'E', 1)

print(dijkstra(graph, 'A'))  # {'A': 0, 'C': 3, 'B': 5, 'E': 4, 'D': 2, 'F': 6}
