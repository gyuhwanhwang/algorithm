import heapq


def solution(jobs):
    heap = []
    time, start, end = 0, 0, len(jobs)
    jobs.sort(reverse=True)  # 도착시간 빠른 것이 오른쪽으로, 같으면 수행시간 짧은 것
    arrive, long = jobs.pop()
    heapq.heappush(heap, (long, arrive))
    start = heap[0][1]  # 처음 작업의 시작시간

    while heap:
        cur = heapq.heappop(heap)
        time += start - cur[1] + cur[0]  # 총 시간 += 시작 - 도착 + 수행
        start += cur[0]  # 빈 시간이 없을 경우 시작시간은 수행시간의 누적
        while jobs and jobs[-1][0] <= start:  # 현재시간 기준 요청 작업 확인
            arrive, long = jobs.pop()
            heapq.heappush(heap, (long, arrive))
        while jobs and not heap:  # 현재와 요청사이의 빈 시간이 있는 경우
            arrive, long = jobs.pop()
            heapq.heappush(heap, (long, arrive))
            start = arrive

    return time // end


import heapq


def solution(jobs):
    heap = []
    jobs = sorted([(job[1], job[0]) for job in jobs], key=lambda x: (-x[1], -x[0]))
    time, start, end = 0, 0, len(jobs)
    heapq.heappush(heap, jobs.pop())
    start = heap[0][1]

    # print(heap)
    while heap:
        cur = heapq.heappop(heap)
        time += start - cur[1] + cur[0]  # 시작 - 도착 + 수행
        start += cur[0]
        while jobs and jobs[-1][1] <= start:
            heapq.heappush(heap, jobs.pop())
        while jobs and not heap:
            heapq.heappush(heap, jobs.pop())
            start = heap[0][1]

    return time // end