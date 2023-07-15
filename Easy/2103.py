class Solution:
    def countPoints(self, rings: str) -> int:
        res = [[],[],[],[],[],[],[],[],[],[]]
        for i in range(0, len(rings), 2):
            res[int(rings[i+1])].append(rings[i])
        count = 0
        for i in res:
            if "R" in i and "G" in i and "B" in i:
                count += 1
        return count