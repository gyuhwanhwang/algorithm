def solution(name):
    change = [min(ord(char) - ord("A"), ord("Z") - ord(char) + 1) for char in name]
    count, cur = 0, 0
    while True:
        count += change[cur]
        change[cur] = 0
        if sum(change) == 0:
            return count

        left, right = -1, 1
        while change[cur + right] == 0:
            right += 1
        while change[cur + left] == 0:
            left -= 1
        cur += right if right <= abs(left) else left
        count += right if right <= abs(left) else -left


solution("JEROEN")