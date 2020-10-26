def solution(n, m):
    if n > m:
        n, m = m, n
    answer = [1, m]
    # 최대 공약수
    for i in range(2, n+1):
        if m % i == 0 and n % i == 0:
            answer[0] = i
    # 최소 공배수
    while True:
        if answer[1] % n == 0:
            break
        answer[1] += m
    return answer