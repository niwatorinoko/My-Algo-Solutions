class Solution:
    def lastVisitedIntegers(self, nums: List[int]) -> List[int]:
        seen, ans = [], []
        p = 0
        for i in nums:
            if i >= 0:
                seen = [i] + seen
                p = 0
            else:
                if p >= len(seen):
                    ans.append(-1)
                else:
                    ans.append(seen[p])
                p += 1
        return ans