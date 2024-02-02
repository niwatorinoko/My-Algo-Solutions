class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        leftCount, rightCount = 0, 0
        for i in s[:len(s)//2]:
            if i in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                leftCount += 1
        for i in s[len(s)//2:]:
            if i in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                rightCount += 1
        return leftCount == rightCount