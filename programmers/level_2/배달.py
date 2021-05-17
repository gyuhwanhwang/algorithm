from collections import defaultdict
import heapq as hq
def solution(N, road, K):
    graph = defaultdict(list)
    for start, end, time in road:
        graph[start].append((time, end))
        graph[end].append((time, start))

    dist = defaultdict(int)
    Q = [(0, 1)]
    answer = 0
    while Q:
        time, node = hq.heappop(Q)
        if time > K: continue
        if node not in dist:
            dist[node] = time
            answer += 1
            for next_time, next_node in graph[node]:
                hq.heappush(Q, (time + next_time, next_node))
    return answer