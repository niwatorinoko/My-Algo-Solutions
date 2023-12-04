class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        for i in range(len(s),1,-1):
            for j in range(len(s)-i+1):
                temp = list(s[j:j+i])
                for k in temp:
                    if chr(ord(k)+32) not in temp:
                        if chr(ord(k)-32) not in temp:
                            break
                else:
                    return s[j:j+i]
        return ""