class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
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
        """
        def expand(right: int, left: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1 : right]

        # 해당사항 없음 필터링
        if len(s) < 2 or s == s[::-1]:
            return s

        # 슬라이딩 윈도우 우측으로 이동
        result = ''
        for i in range(len(s) - 1):
            result = max(result,
                         expand(i, i),
                         expand(i, i + 1),
                         key=len)
        return result


sol = Solution()
sol.longestPalindrome("babad")