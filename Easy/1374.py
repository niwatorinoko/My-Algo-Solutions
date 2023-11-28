class Solution:
    def generateTheString(self, n: int) -> str:
        ans = ""
        if n%2 == 0:
            ans ="q"*(n-1) + "s"
        else:
            ans = "q"*n
        return ans