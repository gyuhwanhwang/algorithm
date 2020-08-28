from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)    # 값에 디폴트로 list

        for word in strs:
            anagrams[''.join(sorted(word))].append(word)
        return anagrams.values()



sol = Solution()
sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
