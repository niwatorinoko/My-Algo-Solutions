class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        ans = 0
        expect = sorted(heights)
        for i in range(len(heights)):
            if heights[i] != expect[i]:
                ans += 1
        return ans