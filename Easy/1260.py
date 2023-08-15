class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        row = len(grid[0])
        arr = []
        for i in grid:
            for j in i:
                arr.append(j)
                
        for i in range(k):
            temp = [arr[-1]]
            del arr[-1]
            arr = temp+arr

        ans = []
        for i in range(0, len(arr), row):
            ans.append(arr[i:i+row])
        return ans