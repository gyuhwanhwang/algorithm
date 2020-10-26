def shorter(left, right, target, hand):
    if sum(divmod(abs(target - left), 3)) < sum(divmod(abs(target - right), 3)):
        return 'L'
    elif sum(divmod(abs(target - left), 3)) > sum(divmod(abs(target - right), 3)):
        return 'R'
    else:
        if hand == 'R':
            return 'R'
        else:
            return 'L'


def solution(numbers, hand):
    hand = 'R' if hand == 'right' else 'L'
    answer = ''
    left, right = 10, 12
    for num in numbers:
        if num in [1, 4, 7]:
            answer += 'L'
            left = num
        elif num in [3, 6, 9]:
            answer += 'R'
            right = num
        else:
            num = 11 if num == 0 else num
            answer += shorter(left, right, num, hand)
            if answer[-1] == 'L':
                left = num
            else:
                right = num
    print(answer)
    return answer