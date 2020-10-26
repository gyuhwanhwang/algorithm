def solution(n):
    three = ""
    answer = 0
    while n >= 3:
        n, R = divmod(n, 3)
        three = str(R) + three
    three = str(n) + three

    for n, number in enumerate(three):
        if number != '0':
            answer += int(number) * 3**n
    return answer