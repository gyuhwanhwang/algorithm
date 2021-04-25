class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for num in [*set(nums1).intersection(set(nums2))]:
            result += [num] * min(nums1.count(num), nums2.count(num))
        return result