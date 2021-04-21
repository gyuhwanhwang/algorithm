from collections import defaultdict


def solution(begin, target, words):
    if target not in words:
        return 0

    graph = defaultdict(list)
    # get graph
    for word in words:
        # iter each word
        for i in range(len(words)):
            # iter each alpha
            if word == words[i] or word == target or words[i] == begin: continue
            count = 0
            for j in range(len(word)):
                if count <= 1 and word[j] != words[i][j]:
                    count += 1
            if count == 1:
                graph[word].append(words[i])
    path = []
    min_path = []

    def dfs(word, path):
        if word == target:
            min_path.append(len(path))

        for next_word in graph[word]:
            if next_word in path:
                continue
            path.append(next_word)
            dfs(next_word, path)
            path.pop()

    for word in words:
        count = 0
        for i in range(len(begin)):
            if count <= 1 and word[i] != begin[i]:
                count += 1
        if count == 1:
            dfs(word, path + [word])
    return min(min_path)