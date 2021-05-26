def solution(numbers):
    answer = []
    for num in numbers:
        if num % 2 == 0:
            answer.append(num + 1)
        else:  # 홀수일 경우 가장 오른쪽 '0'을 찾아 '1'로, 그리고 오른쪽 '1'을 '0'으로 바꿔줌
            binary = list('0' + format(num, 'b'))[::-1]
            idx = binary.index('0')
            binary[idx], binary[idx - 1] = '1', '0'
            answer.append(int(''.join(binary[::-1]), 2))

    return answer