class Solution:
    def minimumMoves(self, s: str) -> int:
        ans = 0
        p = 0
        while p < len(s):
            if s[p] == "O":
                p +=  1
            else:
                ans += 1
                p += 3
        return ans
