from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # 1st
        s.reverse()

        # 2nd
        for i in range(len(s)//2):
            s[i], s[-(i+1)] = s[-(i+1)], s[i]

        s[:] = s[::-1]  # leetcode에 쓰이는 트릭

sol = Solution()
sol.reverseString(["h","e","l","l","o"])