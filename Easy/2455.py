class Solution:
    def averageValue(self, nums: List[int]) -> int:
        ans = []
        for i in nums:
            if i % 3 == 0 and i % 2 == 0:
                ans.append(i)
        if len(ans) == 0:
            return 0
        return sum(ans)//len(ans)