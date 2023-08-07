class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        ans = 0
        for i in hours:
            if target <= i:
                ans += 1
        return ans