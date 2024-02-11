class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        if 1 not in nums:
            return True
        pre_p = nums.index(1)
        for i in range(pre_p+1 ,len(nums)):
            if nums[i] == 1:
                if i-pre_p-1 < k:
                    return False
                else:
                    pre_p = i
        return True