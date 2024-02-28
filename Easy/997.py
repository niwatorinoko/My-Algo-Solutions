class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        out_list = [0]*n
        in_list = [0]*n
        for i, j in trust:
            out_list[i-1] += 1
            in_list[j-1] += 1
        for i in range(1, n+1):
            if out_list[i-1] == 0 and in_list[i-1] == n-1:
                return i
        return -1