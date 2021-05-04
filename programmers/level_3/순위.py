from collections import defaultdict


def solution(n, results):
    def dfs(node, discovered, graph):
        discovered.append(node)
        for w in graph[node]:
            if w not in discovered:
                discovered = dfs(w, discovered, graph)
        return discovered

    win, lose = defaultdict(list), defaultdict(list)
    for w, l in results:
        win[w].append(l)
        lose[l].append(w)

    count = 0
    for i in range(1, n + 1):
        if len(dfs(i, [], win)) + len(dfs(i, [], lose)) == n + 1:
            count += 1
    return count