class Solution:
    def isGood(self, nums: List[int]) -> bool:
        keys = sorted(list(Counter(nums).keys()))

        for i in range(len(keys)-1):
            if keys[i] != i+1:
                return False
        
        if len(keys) == len(nums)-1 and nums.count(len(nums)-1) == 2:
            return True
            
        return False