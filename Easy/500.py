class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        ans = []
        for i in words:
            s = set(i.lower())
            if s <= set("qwertyuiop"):
                ans.append(i)
            if s <= set("asdfghjkl"):
                ans.append(i)
            if s <= set("zxcvbnm"):
                ans.append(i)
        return ans