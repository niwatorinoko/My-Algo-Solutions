class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_index = nums.index(max(nums))
        for i in range(len(nums)):
            if i == max_index:
                continue
            elif nums[i]*2 > nums[max_index]:
                return -1
        return max_index