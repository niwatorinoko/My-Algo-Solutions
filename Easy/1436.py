class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        s, g = [], []
        for i, j in paths:
            s.append(i)
            g.append(j)
        for i in g:
            if i not in s:
                return i
        return paths[-1][-1]