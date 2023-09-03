class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        for i in range(97, 123):
            if abs(word1.count(chr(i)) - word2.count(chr(i))) > 3:
                return False
        return True