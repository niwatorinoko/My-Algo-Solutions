class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        for i in range(k):
            if min(nums) == 0:
                break
            else:
                index = nums.index(min(nums))
                nums[index] = -(nums[index])
        return sum(nums)