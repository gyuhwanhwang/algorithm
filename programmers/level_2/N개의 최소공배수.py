from math import gcd
def solution(arr):
    answer = 1
    for num in arr:
        answer = num * answer // gcd(answer, num)
    return answer