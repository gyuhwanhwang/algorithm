from math import sqrt
from itertools import permutations


def solution(numbers):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

    prime_list = []
    for i in range(1, len(numbers) + 1):
        for p in list(map("".join, permutations(numbers, i))):
            if int(p) not in prime_list and is_prime(int(p)):
                prime_list.append(int(p))
    return len(prime_list)