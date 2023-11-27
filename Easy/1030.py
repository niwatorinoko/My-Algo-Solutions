class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        ans = dict()
        for i in range(rows):
            for j in range(cols):
                ans[(i,j)] = abs(rCenter - i) + abs(cCenter - j)
        ans = sorted(ans.items(), key=lambda x:x[1])
        return [list(i[0]) for i in ans]