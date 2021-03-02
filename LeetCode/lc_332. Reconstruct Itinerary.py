class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        if not tickets:
            return []
        result = []

        ### DFS로 일정 그래프 구성
        graph = collections.defaultdict(list)
        # 그래프 순서대로 구성
        for a, b in sorted(tickets):
            graph[a].append(b)

        route = []

        def dfs(a):
            # 첫 번째 값을 읽어 어휘 순 방문
            while graph[a]:
                dfs(graph[a].pop(0))
            route.append(a)

        dfs("JFK")
        # 다시 뒤집어 어휘 순 결과로
        return route[::-1]

        ### 스택 연산으로 큐 연산 최적화 시도
        graph = collections.defaultdict(list)
        for a, b in sorted(tickets, reverse=True):
            graph[a].append(b)

        route = []

        def dfs(a):
            while graph[a]:
                dfs(graph[a].pop())
            route.append(a)

        dfs("JFK")
        return route[::-1]

        ### 일정 그래프 반복
        graph = collections.defaultdict(list)
        for a, b in sorted(tickets):
            graph[a].append(b)

        route, stack = [], ["JFK"]

        while stack:
            while graph[stack[-1]]:  # 길이 있으면
                stack.append(graph[stack[-1]].pop(0))
            route.append(stack.pop())  # 길이 없으면

        return route[::-1]

#         def dfs(target, cities):
#             for city in cities:
#                 if city[0] == target:
#                     result.append(city[1])
#                     target = city[1]
#                     cities.remove(city)
#                     dfs(target, cities)

#         result = ["JFK"]
#         tickets.sort()
#         print(tickets)
#         dfs("JFK", tickets)
#         return result

#         def dfs(target: str, path: list[str]):
#             if len(path) == (len(tickets) + 1):
#                 result.append(path)
#                 print(result)
#                 return

#             for new_target in graph[target]:
#                 dfs(new_target, path + [new_target])


#         graph = collections.defaultdict(list)
#         for start, end in sorted(tickets):
#             graph[start].append(end)

#         dfs("JFK", ["JFK"])
#         # print(id(result))

#         return result[:]


