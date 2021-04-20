def solution(brown, yellow):
    def max_div(num):
        max_num = 1
        for i in range(1, int(num ** (1 / 2) + 1)):
            if num % i == 0 and ((i + 2) + (num // i)) * 2 == brown:
                max_num = i
        return [max_num, num // max_num]

    return [i + 2 for i in sorted(max_div(yellow), reverse=True)]