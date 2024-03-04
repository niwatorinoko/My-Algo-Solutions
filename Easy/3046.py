class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        nums.sort()
        nums1, nums2 = [], []
        for i in range(0,len(nums),2):
            nums1.append(nums[i])
            nums2.append(nums[i+1])
        for i in range(len(nums1)-1):
            if nums1[i] >= nums1[i+1]:
                return False
        for i in range(len(nums2)-1):
            if nums2[i] >= nums2[i+1]:
                return False
        return True