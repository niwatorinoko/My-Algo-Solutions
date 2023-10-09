class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans = []
        for i, j in Counter(nums).items():
            if len(nums)/3 < j:
                ans.append(i)
        return ans