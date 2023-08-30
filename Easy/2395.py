class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        if len(nums) == 2:
            return False

        sum_li = []
        for i in range(1,len(nums)):
            sum_li.append(nums[i]+nums[i-1])
        
        for i in sum_li:
            if sum_li.count(i) >= 2:
                return True
        return False