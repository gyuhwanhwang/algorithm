import heapq


def solution(scoville, K):
    heapq.heapify(scoville)
    count = 0
    while scoville[0] < K and len(scoville) >= 2:
        count += 1
        heapq.heappush(scoville, heapq.heappop(scoville) + (heapq.heappop(scoville) * 2))

    return count if scoville[0] >= K else -1