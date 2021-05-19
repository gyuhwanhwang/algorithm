def solution(n, t, m, p):
    dict = {
        0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
        10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'
    }

    def trans(num, divi):
        result = ""
        while num >= divi:
            num, other = divmod(num, divi)
            result = dict[other] + result
        result = dict[num] + result
        return result

    return ''.join([trans(i, n) for i in range(t*m)])[p-1::m][:t]