from collections import defaultdict


def solution(tickets):
    graph = defaultdict(list)
    for a, b in sorted(tickets, reverse=True):
        graph[a].append(b)

    path = []

    def dfs(node):
        while graph[node]:
            dfs(graph[node].pop())
        path.append(node)

    dfs("ICN")
    return path[::-1]