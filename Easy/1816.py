class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        s = s.split()
        ans = ""
        for i in range(k):
            ans += s[i] + " "
        
        return ans[:-1]