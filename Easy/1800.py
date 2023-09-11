class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        ans = 0
        for i in range(1,len(nums)+1):
            for j in range(len(nums)-i+1):
                temp = nums[j:i+j]
                if len(set(temp)) != len(temp):
                    continue
                if temp == sorted(temp):
                    if sum(temp) > ans:
                        ans = sum(temp)
                        print(temp,ans)
        
        return ans