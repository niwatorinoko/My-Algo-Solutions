class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        ans = [0, 0]
        for i in range(1, len(nums)+1):
            if c[i] == 2:
                ans[0] = i
            if c[i] == 0:
                ans[1] = i
        return ans