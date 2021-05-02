def solution(number, k):
    stack = [number[0]]
    for num in number[1:]:
        while stack and k > 0 and stack[-1] < num:
            stack.pop()
            k -= 1
        stack.append(num)
    return ''.join(stack[:len(stack) - k])

def solution(number, k):
    # number = list(number)
    p = 0
    while k:
        if p == len(number) - 1:
            number = number[:-1]
            p -= 1
            k -= 1
            continue
        while p + 1 < len(number) and number[p] >= number[p + 1]:
            p += 1
        number = number[:p] + number[p + 1:]
        if p > 0: p -= 1
        k -= 1

    #         for i in range(len(number)-1):
    #             if number[i] < number[i+1]:
    #                 number.pop(i)
    #                 break
    #             if i == len(number) - 2:
    #                 number.pop()

    #         k -= 1
    return "".join(number)

solution("4333", 3)
# print("hi", "4333"[4:])