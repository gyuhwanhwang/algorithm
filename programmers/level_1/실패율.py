def solution(N, stages):
    answer = [0] * N
    stages.sort()
    count = 1
    not_yet = 0
    for i in range(len(stages)):
        if stages[i] == N + 1:
            break
        if i < len(stages)-1 and stages[i] == stages[i+1]:
            count += 1
            continue
        answer[stages[i] -1] = count / (len(stages) - not_yet)
        count, not_yet = 1, i + 1
    return [y for x, y in sorted(zip(answer, range(1, N+1)), key=lambda x: (-x[0], x[1]))]