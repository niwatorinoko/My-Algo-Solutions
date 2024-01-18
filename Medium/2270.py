class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        ans = 0
        l, r = nums[0], sum(nums)-nums[0]
        for i in range(len(nums)-1):
            if l >= r:
                ans += 1
            l += nums[i+1]
            r -= nums[i+1]
        return ans