class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counter = Counter(nums)
        maxFreq = max(counter.values())
        ans = 0
        for i,j in counter.items():
            if j == maxFreq:
                ans += j
        return ans