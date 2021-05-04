from collections import defaultdict
import heapq as hq


def solution(n, edge):
    graph = defaultdict(list)
    for start, end in edge:
        graph[start].append(end)
        graph[end].append(start)

    Q = [(0, 1)]
    dist = defaultdict(int)

    while Q:
        cost, node = hq.heappop(Q)
        if node not in dist:
            dist[node] = cost
            for next_node in graph[node]:
                hq.heappush(Q, (cost + 1, next_node))
    max_val = max(dist.values())
    return sum(True for num in dist.values() if num == max_val)
    # return n - list(dist.values()).index(max_val)