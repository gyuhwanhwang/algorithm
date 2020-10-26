# 1 3 4 5
# 3 1 2 4 5
def solution(answers):
    pattern_1 = [1, 2, 3, 4, 5]                 # len 5
    pattern_2 = [2, 1, 2, 3, 2, 4, 2, 5]     # len 9
    pattern_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]  # len 10
    score = [0] * 3

    for i in range(len(answers)):
        if pattern_1[i % len(pattern_1)] == answers[i]: score[0] += 1
        if pattern_2[i % len(pattern_2)] == answers[i]: score[1] += 1
        if pattern_3[i % len(pattern_3)] == answers[i]: score[2] += 1

    max_score = max(score)
    return [i+1 for i in range(len(score)) if score[i] == max_score]