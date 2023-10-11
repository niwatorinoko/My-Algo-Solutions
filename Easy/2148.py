class Solution:
    def countElements(self, nums: List[int]) -> int:
        ans = 0
        maxNum = max(nums)
        minNum = min(nums)
        for i in nums:
            if maxNum>i and minNum<i:
                ans += 1
        return ans