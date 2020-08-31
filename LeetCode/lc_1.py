from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 1 브루트 포스
        """
        for i in range(len(nums) - 1):
            for j in range(i +1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        """
        # 2 in을 이용한 탐색
        """
        for i, n in enumerate(nums):
            complement = target -n
            if complement in nums[i+1:]:
                return nums.index(n), nums[i+1 : ].index(complement) + (i+1) # 같은 수에 대비 + 뛰어넣은 숫자 더해줌
        """

        #3 첫 번째 수를 뺀 결과 키 조회
        """
        nums_map = {}
        # 키와 값을 바꿔 딕셔너리로 저장
        for i, num in enumerate(nums):
            nums_map[num] = i    # 중복된 값이어도 새로운 인덱스로 대체되어 상관 x

        # 타겟에서 첫 번째 수를 뺀 결과를 키로 조회
        for i, num in enumerate(nums):
            if target - num in nums_map and i != nums_map[target - num]:    # 현재 값 아니어야
                print(nums.index(num), nums_map[target - num])
                return nums.index(num), nums_map[target - num]
        """

        #4 조회 구조 개선
        nums_map = {}
        for i, num in enumerate(nums):
            if target - num in nums_map:
                print(nums_map[target - num], i)
                return nums_map[target - num], i
            nums_map[num] = i

sol = Solution()
sol.twoSum(nums = [3, 3, 3, 3], target = 6)