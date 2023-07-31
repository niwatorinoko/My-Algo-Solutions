class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        w,x,y,z = 0,0,0,0
        w = max(nums)
        nums.remove(max(nums))
        x = max(nums)
        nums.remove(max(nums))
        y = min(nums)
        nums.remove(min(nums))
        z = min(nums)
        nums.remove(min(nums))
        return (w*x)-(y*z)