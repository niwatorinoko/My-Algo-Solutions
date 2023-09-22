class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for i,j in Counter(t).items():
            if s.count(i) != j:
                return i
                