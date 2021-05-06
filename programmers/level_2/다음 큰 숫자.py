def solution(n):
    num_of_1 = bin(n).count('1')
    for num in range(n + 1, 1000001):
        if num_of_1 == bin(num).count('1'):
            return num

    #     def ones(num):
    #         return sum(True for i in bin(num)[2:] if i == '1')

    #     n1 = ones(n)
    #     while True:
    #         n += 1
    #         if n1 == ones(n):
    #             return n