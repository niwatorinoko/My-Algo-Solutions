class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i,j in Counter(nums).items():
            if j >= 2:
                return i