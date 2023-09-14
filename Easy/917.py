class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        ans = []
        only_alpha = []
        for i in s:
            if i.isalpha():
                ans.append("")
                only_alpha.append(i)
            else:
                ans.append(i)
        
        reversed_s = only_alpha[::-1]
        p = 0
        for i in range(len(s)):
            if ans[i] == "":
                ans[i] = reversed_s[p]
                p += 1
        
        res = ""
        for i in ans:
            res += i

        return res