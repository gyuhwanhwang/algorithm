class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 2nd
        max_len = start = 0
        used = {}

        for index, char in enumerate(s):
            # "tmmzuxt"에서 마지막 t 조심
            if char in used and start <= used[char]:
                start = used[char] + 1
            else:
                max_len = max(max_len, index - start + 1)

            used[char] = index

        return max_len

        # 1st
#         if len(s) < 2:
#             return len(s)

#         max_len = 1
#         table = collections.defaultdict(int)
#         left, right = 0, 1
#         table[s[left]] += 1

#         while right < len(s):
#             # print(left, right)
#             # print(table)
#             # 이미 사용된 문자라면
#             if table[s[right]] != 0:
#                 left = left + 1
#                 right = left + 1
#                 """
#                 left = right
#                 rigfht = left + 1
#                 """
#                 # print('여기', left, right)
#                 table = collections.defaultdict(int)
#                 table[s[left]] += 1
#                 continue
#             # 처음 사용
#             table[s[right]] += 1
#             max_len = max(max_len, right - left + 1)
#             right += 1

#         return max_len
