class Solution:
    def modifyString(self, s: str) -> str:
        if s == "?":
            return "a"
        s = list(s)
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        for i in range(len(s)):
            if i == 0 and s[i] == "?":
                p = 0
                while True:
                    if alphabet[p] != s[i+1]:
                        s[0] = alphabet[p]
                        break
                    else:
                        p += 1
            elif i == len(s)-1 and s[i] == "?":
                p = 0
                while True:
                    if alphabet[p] != s[i-1]:
                        s[i] = alphabet[p]
                        break
                    else:
                        p += 1
            elif s[i] == "?":
                p = 0
                while True:
                    if alphabet[p] != s[i-1] and alphabet[p] != s[i+1]:
                        s[i] = alphabet[p]
                        break
                    else:
                        p += 1
        return "".join(s)