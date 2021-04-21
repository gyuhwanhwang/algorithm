from collections import defaultdict


def solution(n, computers):
    # get graph
    graph = defaultdict(list)
    for i in range(n):
        for j in range(n):
            if j != i and computers[i][j] == 1:
                graph[i].append(j)
    visited = set()
    count = 0

    # connect computer
    def dfs(index, connect):
        if index in visited:
            return

        visited.add(index)
        for i in graph[index]:
            if i not in visited and i not in connect:
                connect.append(i)

        for j in connect:
            dfs(j, connect)

    # dfs each computer
    for i in range(n):
        if i not in visited:
            dfs(i, [])
            count += 1
    # 0부터 시작해서 방문한적 없는 노드에서만 카운트를 올려준다

    return count