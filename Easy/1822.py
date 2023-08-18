class Solution:
    def arraySign(self, nums: List[int]) -> int:
        ans = nums[0]
        for i in range(1, len(nums)):
            ans *= nums[i]
        if ans == 0:
            return 0
        elif ans < 0:
            return -1
        return 1