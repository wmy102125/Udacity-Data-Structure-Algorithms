import heapq

minHeap = list()

heapq.heappush(minHeap, (0, 1))

heapq.heappush(minHeap, (-1, 5))

heapq.heappush(minHeap, (2, 0))

heapq.heappush(minHeap, (5, -1))

print("After pushing, now heap looks like: {}".format(minHeap))

# pop and return smallest element from the heap
smallest = heapq.heappop(minHeap)

print("Smallest element in the original list was: {}".format(smallest))
smallest = heapq.heappop(minHeap)

print("Smallest element in the original list was: {}".format(smallest))
smallest = heapq.heappop(minHeap)

print("Smallest element in the original list was: {}".format(smallest))
print("After popping, heap looks like: {}".format(minHeap))


def get_minimum_cost_of_connecting(num_islands, bridge_config):
    """
    :param: num_islands - number of islands
    :param: bridge_config - bridge configuration as explained in the problem statement
    return: cost (int) minimum cost of connecting all islands
    TODO complete this method to returh minimum cost of connecting all islands
    """
    result = {i: float("inf") for i in range(1, num_islands + 1)}
    visited = set()
    # graph =  [[], [(2, 1), (4, 3), (3, 10)], [(1, 1), (3, 4)], [(2, 4), (4, 2), (1, 10)], [(1, 3), (3, 2)]]
    graph = [[]]
    for i in range(1, num_islands + 1):
        arr = []
        for bridge in bridge_config:
            if bridge[0] == i:
                arr.append((bridge[1], bridge[2]))
            if bridge[1] == i:
                arr.append((bridge[0], bridge[2]))
        if arr != []:
            graph.append(arr)
    result[1] = 0
    heapList = []
    heapq.heappush(heapList, (0,1))
    while len(heapList) > 0:
        distance, current_node = heapq.heappop(heapList)
        visited.add(current_node)
        if distance < result[current_node]:
            result[current_node] = distance
        for neighbour in graph[current_node]:
            if neighbour[0] not in visited:
                heapq.heappush(heapList, (neighbour[1], neighbour[0]))
    distance_sum = 0
    for node,distance in result.items():
        if distance == float("inf"):
            continue
        distance_sum += distance
    return distance_sum


"""
:param: num_islands - number of islands
:param: bridge_config - bridge configuration as explained in the problem statement
return: cost (int) minimum cost of connecting all islands
TODO complete this method to returh minimum cost of connecting all islands
"""
# Solution

# The following Solution makes use of one of Python's PriorityQueue implementation (heapq)
# For more details - https://thomas-cokelaer.info/tutorials/python/module_heapq.html
import heapq


def create_graph(num_islands, bridge_config):
    """
    Helper function to create graph using adjacency list implementation
    """
    # A graph can be represented as a adjacency_list, which is a list of blank lists
    graph = [list() for _ in range(num_islands + 1)]

    # populate the adjacency_list
    for config in bridge_config:
        source = config[0]
        destination = config[1]
        cost = config[2]

        # An entry in a sublist of graph is represented as a tuple (neighbor, edge_cost)
        graph[source].append((destination, cost))
        graph[destination].append((source, cost))

    # Try this: print("graph = ",graph)
    return graph


def minimum_cost(graph):
    """
    Helper function to find minimum cost of connecting all islands
    """

    # start with vertex 1 (any vertex can be chosen)
    start_vertex = 1

    # initialize a list to keep track of vertices that are visited
    visited = [False for _ in range(len(graph) + 1)]

    # Heap is represented as a list of tuples
    # A "node" in heap is represented as tuple (edge_cost, neighbor)
    minHeap = [(0, start_vertex)]
    total_cost = 0

    while len(minHeap) > 0:
        # Here, heapq.heappop() will automatically pop out the "node" having smallest edge_cost, and reduce the heap size
        cost, current_vertex = heapq.heappop(minHeap)

        # check if current_vertex is already visited
        if visited[current_vertex]:
            continue

        # else add cost to total-cost
        total_cost += cost

        for neighbor, edge_cost in graph[current_vertex]:
            heapq.heappush(minHeap, (edge_cost, neighbor))

        # mark current vertex as visited
        visited[current_vertex] = True

    return total_cost


def get_minimum_cost_of_connecting_solution(num_islands, bridge_config):
    graph = create_graph(num_islands, bridge_config)
    return minimum_cost(graph)

def test_function(test_case):
    num_islands = test_case[0]
    bridge_config = test_case[1]
    solution = test_case[2]
    output = get_minimum_cost_of_connecting(num_islands, bridge_config)

    if output == solution:
        print("Pass")
    else:
        print("Fail")


# num_islands = 4
# bridge_config = [[1, 2, 1], [2, 3, 4], [1, 4, 3], [4, 3, 2], [1, 3, 10]]
# solution = 6
#
# test_case = [num_islands, bridge_config, solution]
# test_function(test_case)

num_islands = 5
bridge_config = [[1, 2, 5], [1, 3, 8], [2, 3, 9]]
solution = 13

test_case = [num_islands, bridge_config, solution]
test_function(test_case)

# num_islands = 5
# bridge_config = [[1, 2, 3], [1, 5, 9], [2, 3, 10], [4, 3, 9]]
# solution = 31
#
# test_case = [num_islands, bridge_config, solution]
# test_function(test_case)
