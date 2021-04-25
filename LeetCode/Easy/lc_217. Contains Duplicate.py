class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
        # done = set()
        # for i in range(len(nums)):
        #     if nums[i] in done:
        #         return True
        #     done.add(nums[i])
        # return False