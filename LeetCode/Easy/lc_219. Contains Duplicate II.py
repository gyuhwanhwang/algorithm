from collections import defaultdict
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i_dict = defaultdict(list)
        for i in range(len(nums)):
            if not i_dict[nums[i]]:
                i_dict[nums[i]].append(i)
            elif i - i_dict[nums[i]][0] <= k:
                return True
            else:
                i_dict[nums[i]][0] = i
        return False