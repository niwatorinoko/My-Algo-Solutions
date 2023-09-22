class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        li = list(s)
        l, r = 0, len(s)-1
        while l < r:
            if li[l] != li[r]:
                if ascii(li[l]) < ascii(li[r]):
                    li[r] = li[l]
                else:
                    li[l] = li[r]
            l += 1
            r -= 1
        
        return "".join(li)