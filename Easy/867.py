class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = m,n=len(matrix), len(matrix[0])
        res = [[None] * m for _ in range(n)]
        print(res)
        
        for i in range(m):
            for j in range(n):
                print(i, j)
                res[j][i]=matrix[i][j]
        return res