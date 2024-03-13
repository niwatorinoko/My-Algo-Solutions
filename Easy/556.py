class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        nums = []
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                nums.append(mat[i][j])
        if r*c != len(nums):
            return mat
        ans = []
        for i in range(0, len(nums), c):
            print(nums[i:i+c])
            ans.append(nums[i:i+c])
        return ans