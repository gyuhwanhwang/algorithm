from collections import defaultdict


class Solution:
    def isHappy(self, n: int) -> bool:
        done = set()
        while n not in done:
            done.add(n)
            n = sum(i * i for i in map(int, str(n)))
        return n == 1

#         visited = defaultdict(int)
#         result = []

#         def happy(num):
#             if num == 1:
#                 result.append(True)
#                 return
#             visited[num] += 1
#             if visited[num] == 2:
#                 result.append(False)
#                 return
#             val = sum([int(str(num)[i]) ** 2 for i in range(len(str(num)))])
#             # print(val, result)
#             happy(val)

#         happy(n)
#         return result[0]