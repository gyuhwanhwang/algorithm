import collections
def solution(d, budget):
    remain = collections.deque(sorted(d))
    while remain and budget >= remain[0]:
        budget -= remain[0]
        remain.popleft()
    return len(d) - len(remain)