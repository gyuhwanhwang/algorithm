def solution(n, words):
    answer = [0, 0]
    prev = set()
    prev.add(words[0])
    prev_str = words[0][-1]
    for i in range(1, len(words)):
        if words[i] not in prev and words[i][0] == prev_str:
            prev.add(words[i])
            prev_str = words[i][-1]
        else:
            return [i%n + 1, i//n + 1]
    return answer