class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        W1 = ""
        for i in word1:
            W1 += i
        W2 = ""
        for i in word2:
            W2 += i
        return W1 == W2