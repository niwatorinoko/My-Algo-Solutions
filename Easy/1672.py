class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ans = 0
        for i in accounts:
            if ans < sum(i):
                ans = sum(i)

        return ans