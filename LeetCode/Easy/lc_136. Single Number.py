﻿from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for key, val in Counter(nums).items():
            if val == 1:
                return key