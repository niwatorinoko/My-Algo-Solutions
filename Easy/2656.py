class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        maxNum = max(nums)
        res = 0
        for i in range(k):
            res += maxNum+i
        return res