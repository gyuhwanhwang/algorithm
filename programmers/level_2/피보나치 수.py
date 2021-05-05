import sys

sys.setrecursionlimit(10 ** 8)


def solution(n):
    ### 바텀업 방식
    dp = [0] * (n + 1)
    dp[1], dp[2] = 1, 1

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n] % 1234567

    ### 탑다운 방식
    def fibo(x):
        if x == 1 or x == 2:
            return 1
        if dp[x] != 0:  # 이미 계산한 적 있으면 그대로 반환
            return dp[x]
        dp[x] = fibo(x - 1) + fibo(x - 2)
        return dp[x]

    dp = [0] * (n + 1)
    return fibo(n) % 1234567
