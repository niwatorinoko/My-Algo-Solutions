class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        row = []
        for i in matrix:
            row.append(min(i))
        
        col = []
        for i in range(len(matrix[0])):
            temp = []
            for j in range(len(matrix)):
                temp.append(matrix[j][i])
            col.append(max(temp))
        
        for i in row:
            if i in col:
                return [i]