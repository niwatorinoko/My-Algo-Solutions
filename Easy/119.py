class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        triangle = [[1],[1,1]]

        if rowIndex < 1:
            return triangle[rowIndex]
        
        for i in range(2, rowIndex+1):
            temp = []
            for j in range(i+1):
                if j == 0 or j == i:
                    temp.append(1)
                else:
                    temp.append(triangle[i-1][j-1]+triangle[i-1][j])
            triangle.append(temp)
        return triangle[-1]