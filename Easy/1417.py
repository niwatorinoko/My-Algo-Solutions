class Solution:
    def reformat(self, s: str) -> str:
        s_li, n_li = [], []
        for i in s:
            if i.isdigit():
                n_li.append(i)
            else:
                s_li.append(i)
        print(len(s_li)-len(n_li))
        if abs(len(s_li)-len(n_li)) >= 2:
            return ""
        
        ans = ""
        if len(s_li) > len(n_li):
            for i in range(len(n_li)):
                ans += s_li[i]
                ans += n_li[i]
            ans += s_li[-1]
            return ans
        elif len(s_li) < len(n_li):
            for i in range(len(s_li)):
                ans += n_li[i]
                ans += s_li[i]
            ans += n_li[-1]
            return ans
        else:
            for i in range(len(s_li)):
                ans += n_li[i]
                ans += s_li[i]
            return ans