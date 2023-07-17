class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPalindorme(word):
            l = 0
            r = len(word)-1
            while l <= r:
                if word[l] != word[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        for i in range(len(s), 0, -1):
            for j in range(len(s)-i+1):
                if isPalindorme(s[j:j+i]):
                    return s[j:j+i]