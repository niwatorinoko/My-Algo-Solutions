class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        def check(w):
            if set(Counter(w).keys()) == {"a","e","i","o","u"}:
                return True
            return False

        ans = 0
        
        for i in range(5,len(word)+1):
            for j in range(len(word)-i+1):
                if check(word[j:j+i]):
                    ans += 1
        return ans