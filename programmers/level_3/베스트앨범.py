from collections import defaultdict


def solution(genres, plays):
    def order(a):
        return sum(i[0] for i in hash[a])

    result = []
    hash = defaultdict(list)
    for genre, play, i in sorted(zip(genres, plays, range(len(plays))), key=lambda x: (x[1], -x[2])):
        hash[genre].append((play, i))

    for key in sorted(hash.keys(), key=order, reverse=True):
        for _ in range(2):
            if hash[key]:
                result.append(hash[key].pop()[1])
    return result