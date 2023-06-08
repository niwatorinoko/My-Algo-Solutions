class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m*n:
            return []
        res = []
        p = 0
        for i in range(m):
            li = []
            for i in range(n):
                li.append(original[p])
                p += 1
            res.append(li)
        return res