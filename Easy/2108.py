class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def isPalindorome(word):
            l, r = 0, len(word)-1
            while l<r:
                if word[l] != word[r]:
                    return False
                l += 1
                r -= 1
            return True

        for i in words:
            if isPalindorome(i):
                return i
        else:
            return ""
