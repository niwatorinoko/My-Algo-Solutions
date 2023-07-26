class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in set(nums):
            for j in range(nums.count(i)-1):
                nums.remove(i)