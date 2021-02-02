class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # 4th
        return sum(stone in jewels for stone in stones)

        # 3th
#         freqs = collections.Counter(stones)
#         count = 0

#         for jewel in jewels:
#             count += freqs[jewel]

#         return count

# 2nd
#         freqs = collections.defaultdict(int)
#         count = 0

#         for stone in stones:
#             freqs[stone] += 1

#         for jewel in jewels:
#             count += freqs[jewel]

#         return count

# 1st
#         table = {}

#         for jewel in jewels:
#             table[jewel] = 0

#         for stone in stones:
#             if stone in table:
#                 table[stone] += 1

#         return sum(table.values())