class Solution:
    def makeGood(self, s: str) -> str:
        s = list(s)
        p = 0
        while p < len(s)-1:
            if abs(ord(s[p])-ord(s[p+1])) == 32:
                s.pop(p+1)
                s.pop(p)
                p = 0
            else:
                p += 1
        return "".join(s)