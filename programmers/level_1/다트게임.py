import re
def solution(dartResult):
    # bonus = {'S': 1, 'D': 2, 'T':3}
    # option = {'': 1, '*': 2, '#':-1}
    # score = re.findall('(\d+)([SDT])([*#]?)', dartResult)
    # for i in range(len(score)):
    #     if score[i][2] == '*' and i > 0:
    #         score[i-1] *= 2
    #     score[i] = int(score[i][0]) ** bonus[score[i][1]] * option[score[i][2]]
    # return sum(score)

    answer = [0] * 4
    num = 0
    for i in range(len(dartResult)):
        if dartResult[i].isdigit() and dartResult[i-1] != '1':
            num += 1
            if dartResult[i+1] == '0':
                answer[num] = 10
            else:
                answer[num] = int(dartResult[i])
        elif dartResult[i].isalpha():
            if dartResult[i] == 'D':
                answer[num] **= 2
            elif dartResult[i] == 'T':
                answer[num] **= 3
        else:
            if dartResult[i] == '*':
                answer[num] *= 2
                if num != 0:
                    answer[num-1] *= 2
            elif dartResult[i] == '#':
                answer[num] *= -1
    return sum(answer)