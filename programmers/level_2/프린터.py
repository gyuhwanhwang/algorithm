from collections import deque
def solution(priorities, location):
    Q = deque(enumerate(priorities))
    count = 0
    while Q:
        lo, prior = Q.popleft()
        # if not Q or prior >= max(Q, key = lambda x: x[1])[1]:
        # if prior >= max(Q, key = lambda x: x[1], default=(-1, 0))[1]:
        if any(prior < q[1] for q in Q):
            Q.append((lo, prior))
        else:
            count += 1
            if lo == location:
                return count