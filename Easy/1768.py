class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        def merge(word1, word2, l, r):
            ans = ""

            for i in range(r):
                ans += word1[i]
                ans += word2[i]

            if len(word1) > len(word2):
                for j in range(r, l):
                    ans += word1[j]
            if len(word2) > len(word1):
                for j in range(r, l):
                    ans += word2[j]
            return ans
        
        return merge(word1, word2, max(len(word1),len(word2)), min(len(word1),len(word2)))