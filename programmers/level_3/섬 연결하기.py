from collections import defaultdict
import heapq


def solution(n, costs):
    graph = defaultdict(list)
    for start, end, cost in costs:
        graph[start].append((end, cost))
        graph[end].append((start, cost))

    Q = [(0, 0)]  # (소요시간, 도착)
    answer = 0
    visited = set()

    while len(visited) != n:
        cost, end = heapq.heappop(Q)
        if end not in visited:
            visited.add(end)
            answer += cost
            for index, value in graph[end]:
                if index not in visited:
                    heapq.heappush(Q, (value, index))  # cost, to

    return answer


def solution(n, costs):
    def find_parent(x):
        if parents[x] != x:
            parents[x] = find_parent(parents[x]) # 경로압축
        return parents[x]
        # return x if parents[x] == x else find_parent(parents[x])

    answer = 0
    costs = sorted((cost[2], cost[0], cost[1]) for cost in costs)
    parents = [i for i in range(n)]
    visit = 0
    for cost, start, end in costs:
        if find_parent(start) != find_parent(end):
            answer += cost
            parents[find_parent(end)] = find_parent(start)  # union
            visit += 1
        if visit == n - 1:
            return answer