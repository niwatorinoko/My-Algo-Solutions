class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums = sorted(nums)
        ans = 0
        print(len(nums)//2)
        for i in nums:
            if i != nums[len(nums)//2]:
                ans += abs(i-nums[len(nums)//2])
        return ans