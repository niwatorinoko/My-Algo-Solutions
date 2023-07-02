class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        res = []
        ss = s1+ " " +s2
        ss = ss.split()
        for i in ss:
            if ss.count(i) == 1:
                res.append(i)
        return res
        