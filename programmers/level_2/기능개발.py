import math

def solution(progresses, speeds):
    days = []
    result = []
    # get each complete days
    days = [math.ceil((100 - progresses[i]) / speeds[i]) for i in range(len(progresses))]

    while days:
        count = 1
        for i in range(1, len(days)):
            if days[0] >= days[i]:  # if right is done
                count += 1
            else:
                break
        days = days[count:]  # pops done list
        result.append(count)
    return result

    Q = []
    for p, s in zip(progresses, speeds):
        if len(Q) == 0 or Q[-1][0] < -((p - 100) // s):
            Q.append([-((p - 100) // s), 1])
        else:
            Q[-1][1] += 1
    return [q[1] for q in Q]