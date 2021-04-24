import re
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        first = s[:len(s)//2].lower()
        second = s[len(s)//2:].lower()
        return len(re.findall("[aeiou]", first)) == len(re.findall("[aeiou]", second))