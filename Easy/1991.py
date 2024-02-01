class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        leftSum = 0
        rightSum = sum(nums[1:])
        for i in range(len(nums)-1):
            print(leftSum,rightSum)
            if leftSum == rightSum:
                return i
            leftSum += nums[i]
            rightSum -= nums[i+1]
        if leftSum == rightSum:
            return len(nums)-1
        return -1