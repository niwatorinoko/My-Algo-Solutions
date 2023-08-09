class Solution:
    def reverseWords(self, s: str) -> str:
        def reverse_str(s):
            temp = ""
            for i in range(1, len(s)+1):
                temp += s[-i]
            return temp
        s_li = s.split()
        ans_li = []
        for i in s_li:
            ans_li.append(reverse_str(i))
        ans = ""
        for i in range(len(ans_li)-1):
            ans += ans_li[i] + " "
        return ans+ans_li[-1]