class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closest = nums[0]
        for i in range(1, len(nums)):
            if abs(nums[i]) <= abs(closest):
                closest = nums[i]
        if abs(closest) in nums:
            return abs(closest)
        return closest