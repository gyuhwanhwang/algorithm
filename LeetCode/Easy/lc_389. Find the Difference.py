from collections import Counter


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_dict, t_dict = Counter(s), Counter(t)

        for key, value in t_dict.items():
            if value != s_dict[key]:
                return key389. Find the Difference389. Find the Difference