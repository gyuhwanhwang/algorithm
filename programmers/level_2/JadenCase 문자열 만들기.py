def solution(s):
    answer = []
    for string in s.lower().split(' '):
        answer.append(string.capitalize())
    return " ".join(answer)