class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 2nd
        freqs = collections.Counter(nums)
        freqs_heap = []

        for f in freqs:
            # 등장횟수의 음수가 키가 되게
            heapq.heappush(freqs_heap, (-freqs[f], f))

        topk = []
        for _ in range(k):
            topk.append(heapq.heappop(freqs_heap)[1])

        return topk

        # 1st
        counter = collections.Counter(nums)
        return [n for n, _ in counter.most_common(k)]