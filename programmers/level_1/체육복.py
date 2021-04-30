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

def solution(n, lost, reserve):
    while reserve:
        num = reserve.pop()
        if num in lost:
            lost.remove(num)
            continue
        if num-1 not in reserve and num - 1 in lost:
            lost.remove(num-1)
            continue
        if num+1 not in reserve and num + 1 in lost:
            lost.remove(num+1)
            continue
    return n - len(lost)

def solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)