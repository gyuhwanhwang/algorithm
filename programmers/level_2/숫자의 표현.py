def solution(n):
    count = 1 if n % 2 == 0 else 2  # 짝수인 경우 자기 자신만, 홀 수 인경우 //2 -1, +1
    for i in range(3, int(n ** 1 / 2) + 1, 2):  # 홀 수로 나눠질때마다
        if n % i == 0:
            count += 1

    return count