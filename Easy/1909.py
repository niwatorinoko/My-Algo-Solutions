class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        dnums = nums.copy()
        for i in range(len(nums)):
            temp = dnums.copy()
            temp.pop(i)
    
            if sorted(temp) == temp and len(temp) == len(set(temp)):
                print(temp)
                return True
        return False