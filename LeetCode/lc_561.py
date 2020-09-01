from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # 1 pythonic way
        return sum(sorted(nums)[::2])

        # 짝수번째 계산
        # nums.sort()
        # pairs = [nums[i] for i in range(len(nums)) if i % 2 == 0]
        # return sum(pairs)

        # sum = 0
        # nums.sort()
        # for i, n in enumerate(nums):
        #     if i % 2 == 0:
        #         sum += n
        # return sum


sol = Solution()
sol.arrayPairSum([1, 2])