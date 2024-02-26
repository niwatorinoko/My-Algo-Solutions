class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix = []
        count = 0
        for i in range(len(nums)):
            count += nums[i]
            prefix.append(count)
        if min(prefix) < 0:
            return abs(min(prefix))+1
        return 1

        return 0