class Solution:
    def replaceDigits(self, s: str) -> str:
        """
        ans = ""
        for i in range(0,len(s)-1,2):
            print(chr(ord(s[i])+int(s[i+1])))
            ans += s[i]+chr(ord(s[i])+int(s[i+1]))
        if len(s)%2 == 1:
            ans += s[-1]
        return ans
        """
        ans = list(s)
        for i in range(1, len(s), 2):
            ans[i] = chr(ord(s[i-1])+int(s[i]))
        return "".join(ans)