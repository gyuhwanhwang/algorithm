def solution(n):
    pattern = ['1', '2', '4']
    answer = ""

    while n > 0:
        n -= 1
        n, R = divmod(n, 3)
        answer = pattern[R] + answer

    return answer
    # R_pattern = {0: '1', 1: '2', 2: '4'}
    # n_pattern = {1: '1', 2: '2', 3: '4'}
    # n -= 1
    # n, R = divmod(n, 3)
    # if n < 4 :
    #     answer = n_pattern[n] + R_pattern[R] if n > 0 else R_pattern[R]
    # else : # n > 3
    #     answer = R_pattern[R]
    #     while n > 3:
    #         n, R = divmod(n, 3)
    #         if R == 0:
    #             n -= 1
    #             R += 3
    #         answer = n_pattern[R] + answer
    #     answer = n_pattern[n] + answer
    # return answer
