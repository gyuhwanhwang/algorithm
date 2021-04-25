class Solution:
    def countPrimes(self, n: int) -> int:
        answer = [True] * n
        for i in range(2, int(n ** 0.5) + 1):
            if answer[i]:
                for j in range(i + i, n, i):
                    answer[j] = False

        # return len([i for i in range(2, n) if answer[i] == True])
        return sum(answer[2:n])
