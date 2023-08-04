class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        count = list(Counter(nums).keys())
        if len(count) < 3:
            return max(count)
        count.remove(max(count))
        count.remove(max(count))
        return max(count)