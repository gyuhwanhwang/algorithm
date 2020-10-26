def solution(n, lost, reserve):
    answer = n - len(lost)
    # 체육복 여분있는데 도난당한애들
    for l in lost:
        if l in reserve:
            lost[lost.index(l)] = -1
            reserve[reserve.index(l)] = -1
            answer += 1
    # 체육복 여분없이 도난당한애들
    for l in lost:
        if l-1 in reserve:
            answer += 1
            reserve[reserve.index(l-1)] = -1
        elif l+1 in reserve:
            answer += 1
            reserve[reserve.index(l+1)] = -1
    return answer