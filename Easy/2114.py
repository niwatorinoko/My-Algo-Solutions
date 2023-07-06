class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        res = 0
        for i in sentences:
            if len(i.split()) >= res:
                res = len(i.split())
        return res