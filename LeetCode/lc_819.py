from typing import List
from collections import Counter, defaultdict
import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:

        #1
        """"
        result = paragraph.lower()
        result = re.sub('[^a-z]', ' ', result)
        counter = Counter(result.split())
        for k, v in counter.most_common(len(counter)):
            if k not in banned:
                return k
        """

        #2
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split()
                    if word not in banned]
        """
        counts = defaultdict(int)
        for word in words:
            counts[word] += 1

        print(max(counts, key=counts.get))
        # print(max(counts, key=lambda x: counts[x]))
        """

        #3
        counts = Counter(words)
        return counts.most_common(1)[0][0]


sol = Solution()
sol.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"])
