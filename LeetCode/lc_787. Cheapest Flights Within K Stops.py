class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = collections.defaultdict(list)
        # 그래프 인접 리스트 구성
        for u, v, w in flights:
            graph[u].append((v, w))

        # 큐 변수: [(가격, 정점, 남은 가능 경유지 수)]
        Q = [(0, src, K)]

        # 우선순위 큐 최솟값 기준으로 도착점까지 최소 비용 판별
        while Q:
            price, node, k = heapq.heappop(Q)
            if node == dst:
                return price
            if k >= 0:
                for v, w in graph[node]:
                    alt = price + w
                    heapq.heappush(Q, (alt, v, k - 1))

        return -1

        ### me
        graph = collections.defaultdict(list)
        for s, d, c in flights:
            graph[s].append((c, d))

        # visited = set()
        middle = -1
        Q = [(0, src, middle)]
        # result = sys.maxsize
        while Q:
            cost, node, mid = heapq.heappop(Q)
            if mid > K:
                continue

            # @잘못@ 목적지이면서 경유 횟수가 적거나 같을때
            # if node == dst and mid <= K and cost < result:
            #     result = cost

            if node == dst:
                return cost

            for next_cost, next_dst in graph[node]:
                alt = next_cost + cost
                heapq.heappush(Q, (alt, next_dst, mid + 1))

        # if result < sys.maxsize:
        # return result
        return -1

