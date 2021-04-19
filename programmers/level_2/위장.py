from collections import defaultdict


def solution(clothes):
    cloth_dict = defaultdict(list)
    # save each cloth
    for cloth in clothes:
        cloth_dict[cloth[1]].append(cloth[0])

    # answer = (len(first) + 1) * (len(second) + 1) ... - 1 (none)
    answer = 1
    for cloth in cloth_dict:
        answer *= len(cloth_dict[cloth]) + 1

    return answer - 1