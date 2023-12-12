class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        for i in range(len(nums)-1):
            temp = []
            for j in range(len(nums)-1):
                temp.append((nums[j] + nums[j+1]) % 10)
            nums = temp

        return nums[0]