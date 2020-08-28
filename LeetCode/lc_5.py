class Solution:
    def longestPalindrome(self, s: str) -> str:
        left = len(s)
        for i in range(len(s)):
            for j in range(i+1):
                # print(s[-1:-6:-1])
                # print(i,j, s[j:j+left:-1])
                if s[j:j+left] == s[-(i+1)+j:-(len(s)+1)+j:-1]:
                    # print(s[j:j+left])
                    return s[j:j+left]
            left -= 1
        if left == 0:
            return ""

sol = Solution()
sol.longestPalindrome("babad")