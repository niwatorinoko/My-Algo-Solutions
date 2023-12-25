class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return []
        nums = sorted(nums)
        index = nums.index(target)

        return [i for i in range(index, index+nums.count(target))]