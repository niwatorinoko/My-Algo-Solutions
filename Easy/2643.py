class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        ans = [0,0]
        for i in range(len(mat)):
            if sum(mat[i]) > ans[1]:
                ans = [i,sum(mat[i])]
        return ans