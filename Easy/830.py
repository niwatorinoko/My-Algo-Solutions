class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        ans = []
        start = 0
        i = 0
        for i in range(1, len(s)):
            if s[start] != s[i]:
                if i - start >= 3:
                    ans.append([start, i-1])
                start = i
        if i - start >= 2:
            ans.append([start, i])
        return ans