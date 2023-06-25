class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if a == b:
            return -1

        if len(a) > len(b):
            max_len = len(a)
            longer_str = a
            shorter_str = b
        else:
            max_len = len(b)
            longer_str = b
            shorter_str = a            

        for i in range(max_len,0,-1):
            for j in range(max_len+1-i):
                if longer_str[j:j+i] not in shorter_str:
                    return i