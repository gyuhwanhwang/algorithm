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

def solution(tickets):
    graph = defaultdict(list)
    for a, b in sorted(tickets, reverse=True):
        graph[a].append(b)

    stack, path = ["ICN"], []
    while stack:
        while graph[stack[-1]]:
            stack.append(graph[stack[-1]].pop())
        # 막히는 부분에서 풀어냄
        path.append(stack.pop())
    return path[::-1]