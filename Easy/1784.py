class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        for i in range(len(s)):
            if s[i] == "0":
                c = i
                break
        else:
            return True
        if int(s[c:]) > 0:
            return False
        return True