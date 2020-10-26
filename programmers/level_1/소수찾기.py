def solution(n):
    answer = [False, False] + [True] * (n-1)
    for i in range(2, int(n**(1/2)) + 1):
        if answer[i] == True:
            for j in range(i+i, n+1, i):
                answer[j] = False
    return sum(answer)