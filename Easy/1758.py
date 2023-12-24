class Solution:
    def minOperations(self, s: str) -> int:
        p1, p2 = 0, 0
        for i in range(len(s)):
            if i%2 == 0:
                if s[i] == "0":
                    p1 += 1
                else:
                    p2 += 1
            else:
                if s[i] == "1":
                    p1 += 1
                else:
                    p2 += 1
        return min(p1,p2)