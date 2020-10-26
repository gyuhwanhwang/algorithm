def solution(s):
    # 홀수인경우
    if len(s) % 2 != 0:
        return s[len(s)//2]
    # 짝수인 경우
    else :
        return s[(len(s)//2) - 1 : (len(s)//2) + 1]