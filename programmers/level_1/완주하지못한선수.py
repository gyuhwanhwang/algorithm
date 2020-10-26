from collections import defaultdict, Counter
def solution(participant, completion):
    answer = Counter(participant) - Counter(completion)
    return list(answer.keys())[0]
    # count_p, count_c = defaultdict(int), defaultdict(int)
    # for p in participant:
    #     count_p[p] += 1
    # for c in completion:
    #     count_c[c] += 1
    # for p in count_p:
    #     if count_p[p] != count_c[p]:
    #         return p