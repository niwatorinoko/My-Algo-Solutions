class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        st = ""
        count = {}
        for i in paragraph:
            if i.isalpha():
                st += i.lower()
            else:
                if st not in banned and len(st)>0:
                    if st in count:
                        count[st] += 1
                    else:
                        count[st] = 1
                st = ""
        if st not in banned and len(st)>0:
            if st in count:
                count[st] += 1
            else:
                count[st] = 1

        ans = ["",0]
        for i, j in count.items():
            if j > ans[1]:
                ans = [i,j]
        
        return ans[0]