class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        zero_count = 0
        one_count = 0
        for i in range(len(s),0,-1):
            for j in range(len(s)-i+1):
                if set(s[j:j+i]) == {'0'}:
                    zero_count = len(s[j:j+i])
                elif set(s[j:j+i]) == {'1'}:
                    one_count = len(s[j:j+i])
            if zero_count < one_count:
                return True
        return False