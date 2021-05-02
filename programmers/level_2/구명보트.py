def solution(people, limit):
    people.sort()
    left, right = 0, len(people) - 1
    count = 0
    while left < right:
        while right >= 1 and people[left] + people[right] > limit:
            right -= 1
        if left < right:
            count += 1
            people[left], people[right] = 0, 0
            left, right = left + 1, right - 1
    return count + sum(bool(p) for p in people)

def solution(people, limit) :
    answer = 0
    people.sort()

    a = 0
    b = len(people) - 1
    while a < b :
        if people[b] + people[a] <= limit :
            a += 1
            answer += 1
        b -= 1
    return len(people) - answer