class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        res = 0
        for i in range(len(grid)):
            temp = []
            for j in range(len(grid)):
                temp.append(grid[j][i])
            res += grid.count(temp)
        return res