class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        ans = 0
        for word in words:
            if set(word) <= set(allowed):
                ans += 1
        return ans