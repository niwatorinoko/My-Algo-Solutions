class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        maxlength = 1
        l = 1
        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                l += 1
            else:
                maxlength = max(l, maxlength)
                l = 1
        maxlength = max(l, maxlength)
        return maxlength