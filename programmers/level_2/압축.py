def solution(msg):
    dict = {}
    for i in range(26):
        dict[chr(ord('A') + i)] = i+1
    i, left = 27, 0
    answer = []
    while left < len(msg):
        k = 0
        while left+1+k <= len(msg) and msg[left:left+1+k] in dict:
            k += 1
        answer.append(dict[msg[left:left+1+k - 1]])
        dict[msg[left:left+1+k]] = i
        i += 1
        left += k

    return answer