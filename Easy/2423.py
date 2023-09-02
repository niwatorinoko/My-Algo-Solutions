class Solution:
    def equalFrequency(self, word: str) -> bool:
        def check(w):
            li = list(Counter(w).values())
            n = li[0]
            for i in range(1,len(li)):
                if li[i] != n:
                    return False
            return True
            

        word = list(word)
        ans = 0
        for i in range(len(word)):
            t = ""
            for j in range(len(word)):
                if i == j:
                    continue
                t += word[j]
            if check(t):
                return True
        return False