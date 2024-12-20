import heapq
from math import radians, fabs, cos, asin, sqrt, sin


class Pot:
    def __init__(self, arr, distance, estimate_distance):
        self.arr = arr
        self.distance = distance
        self.estimate_distance = estimate_distance

def shortest_path(M, start, goal):
    all_roads = M.roads
    all_intersections = M.intersections
    paths_queue = []
    heapq.heappush(paths_queue,(0,0,start,[start]))
    explored_set = set()
    explored_set.add(start)
    goal_location = all_intersections[goal]

    while paths_queue:
        estimate_distance,current_distance,current_node,current_path = heapq.heappop(paths_queue)
        if current_node == goal:
            return current_path
        explored_set.add(current_node)
        neighbours = all_roads[current_node]
        current_location = all_intersections[current_node]
        for neighbour in neighbours:
            if neighbour in explored_set:
                continue
            neighbour_distance = get_distance_hav(current_location, all_intersections[neighbour])
            distance = current_distance + neighbour_distance
            estimate_distance =distance + get_distance_hav(goal_location,all_intersections[neighbour])
            heapq.heappush(paths_queue,(estimate_distance,distance,neighbour,current_path + [neighbour]))
    return []



def shortest_path_first(M, start, goal):
    all_roads = M.roads
    all_intersections = M.intersections
    paths = [Pot([start], 0, 0)]
    explorer_set = set()
    explorer_set.add(start)
    goal_location = all_intersections[goal]

    selected_path = paths[0]
    end_distance = 0
    is_end = False
    while is_end is False:
        arr = selected_path.arr
        copy_arr = arr.copy()
        point = arr[len(arr)-1]
        point_location = all_intersections[point]
        neighbours = all_roads[point]
        if point == goal:
            return selected_path.arr
        i = 0
        path_is_circle = True
        for neighbour in neighbours:
            if  neighbour in arr:
                    continue
            path_is_circle = False
            distance = selected_path.distance + get_distance_hav(point_location, all_intersections[neighbour])
            estimate_distance = selected_path.distance + distance + get_distance_hav(goal_location,
                                                                                    all_intersections[neighbour])
            if i == 0:
                selected_path.arr.append(neighbour)
                selected_path.distance = distance
                selected_path.estimate_distance = estimate_distance
            else:
                new_arr = copy_arr.copy()
                new_arr.append(neighbour)
                new_pot = Pot(new_arr, distance, estimate_distance)
                paths.append(new_pot)
            i+=1
        if path_is_circle:
            selected_path.estimate_distance=float("inf")

        min_distance = float("inf")
        for new_path in paths:
            estimate_distance = new_path.estimate_distance
            if min_distance > estimate_distance:
                min_distance = estimate_distance
                selected_path = new_path
        if end_distance == min_distance:
            is_end = True
        else:
            end_distance = min_distance

    return selected_path.arr


def hav(theta):
    s = sin(theta / 2)
    return s * s


def get_distance_hav(pot1, pot2):
    lat0 = pot1[0]
    lng0 = pot1[1]
    lat1 = pot2[0]
    lng1 = pot2[1]
    # 用haversine公式计算球面两点间的距离
    # 经纬度转换成弧度
    lat0 = radians(lat0)
    lat1 = radians(lat1)
    lng0 = radians(lng0)
    lng1 = radians(lng1)
    dlng = fabs(lng0 - lng1)
    dlat = fabs(lat0 - lat1)
    h = hav(dlat) + cos(lat0) * cos(lat1) * hav(dlng)
    distance = 2 * 6378.137 * asin(sqrt(h))  # km
    return distance


class M:
    def __init__(self, roads, intersections):
        self.roads = roads
        self.intersections = intersections


roads = [[36, 34, 31, 28, 17],
         [35, 31, 27, 26, 25, 20, 18, 17, 15, 6],
         [39, 36, 21, 19, 9, 7, 4],
         [35, 20, 15, 11, 6],
         [39, 36, 21, 19, 9, 7, 2],
         [32, 16, 14],
         [35, 20, 15, 11, 1, 3],
         [39, 36, 22, 21, 19, 9, 2, 4],
         [33, 30, 14],
         [36, 21, 19, 2, 4, 7],
         [31, 27, 26, 25, 24, 18, 17, 13],
         [35, 20, 15, 3, 6],
         [37, 34, 31, 28, 22, 17],
         [27, 24, 18, 10],
         [33, 30, 16, 5, 8],
         [35, 31, 26, 25, 20, 17, 1, 3, 6, 11],
         [37, 30, 5, 14],
         [34, 31, 28, 26, 25, 18, 0, 1, 10, 12, 15],
         [31, 27, 26, 25, 24, 1, 10, 13, 17],
         [21, 2, 4, 7, 9],
         [35, 26, 1, 3, 6, 11, 15],
         [2, 4, 7, 9, 19],
         [39, 37, 29, 7, 12],
         [38, 32, 29],
         [27, 10, 13, 18],
         [34, 31, 27, 26, 1, 10, 15, 17, 18],
         [34, 31, 27, 1, 10, 15, 17, 18, 20, 25],
         [31, 1, 10, 13, 18, 24, 25, 26],
         [39, 36, 34, 31, 0, 12, 17],
         [38, 37, 32, 22, 23],
         [33, 8, 14, 16],
         [34, 0, 1, 10, 12, 15, 17, 18, 25, 26, 27, 28],
         [38, 5, 23, 29],
         [8, 14, 30],
         [0, 12, 17, 25, 26, 28, 31],
         [1, 3, 6, 11, 15, 20],
         [39, 0, 2, 4, 7, 9, 28],
         [12, 16, 22, 29],
         [23, 29, 32],
         [2, 4, 7, 22, 28, 36]]

intersections = {0: [0.7801603911549438, 0.49474860768712914],
                 1: [0.5249831588690298, 0.14953665513987202],
                 2: [0.8085335344099086, 0.7696330846542071],
                 3: [0.2599134798656856, 0.14485659826020547],
                 4: [0.7353838928272886, 0.8089961609345658],
                 5: [0.09088671576431506, 0.7222846879290787],
                 6: [0.313999018186756, 0.01876171413125327],
                 7: [0.6824813442515916, 0.8016111783687677],
                 8: [0.20128789391122526, 0.43196344222361227],
                 9: [0.8551947714242674, 0.9011339078096633],
                 10: [0.7581736589784409, 0.24026772497187532],
                 11: [0.25311953895059136, 0.10321622277398101],
                 12: [0.4813859169876731, 0.5006237737207431],
                 13: [0.9112422509614865, 0.1839028760606296],
                 14: [0.04580558670435442, 0.5886703168399895],
                 15: [0.4582523173083307, 0.1735506267461867],
                 16: [0.12939557977525573, 0.690016328140396],
                 17: [0.607698913404794, 0.362322730884702],
                 18: [0.719569201584275, 0.13985272363426526],
                 19: [0.8860336256842246, 0.891868301175821],
                 20: [0.4238357358399233, 0.026771817842421997],
                 21: [0.8252497121120052, 0.9532681441921305],
                 22: [0.47415009287034726, 0.7353428557575755],
                 23: [0.26253385360950576, 0.9768234503830939],
                 24: [0.9363713903322148, 0.13022993020357043],
                 25: [0.6243437191127235, 0.21665962402659544],
                 26: [0.5572917679006295, 0.2083567880838434],
                 27: [0.7482655725962591, 0.12631654071213483],
                 28: [0.6435799740880603, 0.5488515965193208],
                 29: [0.34509802713919313, 0.8800306496459869],
                 30: [0.021423673670808885, 0.4666482714834408],
                 31: [0.640952694324525, 0.3232711412508066],
                 32: [0.17440205342790494, 0.9528527425842739],
                 33: [0.1332965908314021, 0.3996510641743197],
                 34: [0.583993110207876, 0.42704536740474663],
                 35: [0.3073865727705063, 0.09186645974288632],
                 36: [0.740625863119245, 0.68128520136847],
                 37: [0.3345284735051981, 0.6569436279895382],
                 38: [0.17972981733780147, 0.999395685828547],
                 39: [0.6315322816286787, 0.7311657634689946]}
map_40 = M(roads, intersections)

# path = shortest_path(map_40, 5, 34)
# if path == [5, 16, 37, 12, 34]:
#     print("great! Your code works for these inputs!")
# else:
#     print("something is off, your code produced the following:")
#     print(path)
# path = shortest_path(map_40, 8, 24)
# if path == [8, 14, 16, 37, 12, 17, 10, 24]:
#     print("great! Your code works for these inputs!")
# else:
#     print("something is off, your code produced the following:")
#     print(path)


MAP_40_ANSWERS = [
    (5, 34, [5, 16, 37, 12, 34]),
    (5, 5,  [5]),
    (8, 24, [8, 14, 16, 37, 12, 17, 10, 24])
]

def test():
    map_40 =  M(roads, intersections)
    correct = 0
    for start, goal, answer_path in MAP_40_ANSWERS:
        path = shortest_path(map_40, start, goal)
        if path == answer_path:
            correct += 1
        else:
            print("For start:", start,
                  "Goal:     ", goal,
                  "Your path:", path,
                  "Correct:  ", answer_path)
    if correct == len(MAP_40_ANSWERS):
        print("All tests pass! Congratulations!")
    else:
        print("You passed", correct, "/", len(MAP_40_ANSWERS), "test cases")

test()