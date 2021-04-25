from collections import defaultdict
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        table = defaultdict(str)
        s = s.split()
        if len(pattern) != len(s):
            return False
        for i in range(len(pattern)):
            if not table[pattern[i]]:
                if s[i] in table.values():
                    return False
                table[pattern[i]] = s[i]
            elif table[pattern[i]] != s[i]:
                return False
        return True