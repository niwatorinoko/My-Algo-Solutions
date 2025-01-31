class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:

        def countColor(grids):
            w = 0
            b = 0
            for grid in grids:
                if grid == "W":
                    w += 1
                else:
                    b += 1
            return w == 1 or w == 0 or b == 1 or b == 0

        # grid[0][0], grid[0][1], grid[1][0], grid[1][1]
        if countColor([grid[0][0], grid[0][1], grid[1][0], grid[1][1]]):
            return True
        # grid[0][1], grid[0][2], grid[1][1], grid[1][2]
        if countColor([grid[0][1], grid[0][2], grid[1][1], grid[1][2]]):
            return True
        # grid[1][0], grid[1][1], grid[2][0], grid[2][1]
        if countColor([grid[1][0], grid[1][1], grid[2][0], grid[2][1]]):
            return True
        # grid[1][1], grid[1][2], grid[2][1], grid[2][2]
        if countColor([grid[1][1], grid[1][2], grid[2][1], grid[2][2]]):
            return True
        return False