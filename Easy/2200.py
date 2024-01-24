class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        k_index = []
        for i in range(len(nums)):
            if nums[i] == key:
                k_index.append(i)
        k_index = sorted(k_index)
        ans = []
        for i in range(len(nums)):
            for j in k_index:
               if abs(i-j) <= k:
                  ans.append(i)
                  break
        return ans