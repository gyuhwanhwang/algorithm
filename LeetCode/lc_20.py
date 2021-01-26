class Solution:
    def isValid(self, s: str) -> bool:
        # second
        stack = []
        table = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for char in s:
            if char not in table:
                stack.append(char)
            elif not stack or table[char] != stack.pop():
                return False

        return not stack

        # first
#         stack = [s[0]]
#         table = {
#             '{' : '}',
#             '(' : ')',
#             '[' : ']'
#         }

#         for i in range(1, len(s)):
#             stack.append(s[i])
#             if len(stack) > 1 and stack[-2] in table and table[stack[-2]] == stack[-1]:
#                 stack.pop()
#                 stack.pop()

#         return not stack