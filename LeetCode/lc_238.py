from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        p = 1
        # 왼쪽 곱셈
        for i in range(0, len(nums)):
            output.append(p)
            p = p * nums[i]
        p = 1
        # 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈
        for i in range(len(nums) - 1, 0 - 1, -1):
            output[i] = output[i] * p
            p = p * nums[i]
        return output

        # for i in range(len(nums)):
        #     output.append(p)
        #     p = p * nums[i]
        # p = 1
        # for i in range(-1, -len(nums) - 1, -1):
        #     output[i] = output[i] * p
        #     p = p * nums[i]
        # return output

sol = Solution()
sol.productExceptSelf([1,2,3,4])