class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        if len(set(nums1)&set(nums2)) == 0:
            return -1
        return min(set(nums1)&set(nums2))