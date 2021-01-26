class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # third 스택을 이용한 풀이
        counter, seen, stack = collections.Counter(s), set(), []

        for char in s:
            counter[char] -= 1
            if char in seen:
                continue
            # 뒤에 붙일 문자가 남아있다면 스택에서 제거
            while stack and stack[-1] > char and counter[stack[-1]] > 0:
                seen.remove(stack.pop())
            stack.append(char)
            seen.add(char)

        return ''.join(stack)

        # second 재귀를 이용한 분리

#         # 집합으로 정렬
#         for char in sorted(set(s)):
#             suffix = s[s.index(char):]
#             # 전체 집합과 접미사 집합이 일치할 때 분리 진행
#             if set(s) == set(suffix):
#                 return char + self.removeDuplicateLetters(suffix.replace(char, ''))
#         return ''

# first
#         stack = []

#         for i, char in enumerate(s):
#             if not stack:
#                 stack.append(char)
#                 continue

#             while stack and char not in stack and stack[-1] > char and stack[-1] in s[i+1:]:
#                 stack.pop()
#             if char not in stack:
#                 stack.append(char)

#         return ''.join(stack)

