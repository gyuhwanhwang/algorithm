def solution(skill, skill_trees):
    answer = 0
    for tree in skill_trees:
        cur = 0
        for i in range(len(tree) + 1):
            if i == len(tree):
                answer += 1
                break
            if tree[i] not in skill:
                continue
            elif tree[i] == skill[cur]:
                cur += 1
            else:
                break
    return answer


solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"])