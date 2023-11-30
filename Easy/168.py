class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = ""
        while columnNumber > 26:
            columnNumber -= 1
            s = chr(columnNumber%26+65)
            ans = s + ans
            columnNumber = columnNumber//26
        ans = chr(columnNumber+64) + ans
        return ans