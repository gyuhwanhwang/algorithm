from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        odd = sum(val & 1 for key, val in Counter(s).items())
        return len(s) - odd + 1 if odd > 1 else len(s)

    def longestPalindrome(self, s):
        odds = sum(v & 1 for v in collections.Counter(s).values())
        return len(s) - odds + bool(odds)