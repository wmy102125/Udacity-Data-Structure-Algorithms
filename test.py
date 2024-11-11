import heapq
import collections


def networkDelayTime(times, n, K):
    # Step 1: 构建邻接表
    graph = collections.defaultdict(list)
    for u, v, w in times:
        graph[u].append((v, w))

    # Step 2: 使用 Dijkstra 算法初始化最短路径表
    min_time = {i: float('inf') for i in range(1, n + 1)}
    min_time[K] = 0  # 起点到自身的距离为 0

    # Step 3: 使用优先队列（小顶堆）来进行 Dijkstra 计算
    queue = [(0, K)]  # (当前距离, 节点)
    while queue:
        time, node = heapq.heappop(queue)

        # 如果当前时间大于已记录的最短时间，跳过
        if time > min_time[node]:
            continue

        # 更新邻接节点的距离
        for neighbor, travel_time in graph[node]:
            new_time = time + travel_time
            # 如果找到更短的路径，更新距离表
            if new_time < min_time[neighbor]:
                min_time[neighbor] = new_time
                heapq.heappush(queue, (new_time, neighbor))

    # Step 4: 找到最短路径表中最大值（即信号传播到所有节点的时间）
    max_time = max(min_time.values())
    return max_time if max_time < float('inf') else -1
times = [[2, 1, 1], [2, 3, 1], [3, 4, 1], [2, 5, 1]]
n = 5
K = 2
print(networkDelayTime(times, n, K))  # 输出: 2