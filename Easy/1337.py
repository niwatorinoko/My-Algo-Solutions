class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        res = dict()
        for i in range(len(mat)):
            res[i] = sum(mat[i])
        res = dict(sorted(res.items(), key=lambda item: item[1]))
        ans = list(res.keys())
        return ans[:k]