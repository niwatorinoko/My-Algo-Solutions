class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        ans = ""
        count = 1
        for i in sentence.split():
            temp = ""
            if i[0] in ["a","e","i","o","u","A","E","I","O","U"]:
                temp = i + "ma" + "a"*count
            else:
                temp = i[1:]+ i[0] + "ma" + "a"*count
            count += 1
            ans += temp + " "

        return ans[:-1]