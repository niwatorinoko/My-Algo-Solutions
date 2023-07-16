class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        ans = []
        for i in range(1, max(max(nums1), max(nums2), max(nums3))+1):
            count = 0
            if i in nums1:
                count += 1
            if i in nums2:
                count += 1
            if i in nums3:
                count += 1
            if count >= 2:
                ans.append(i)
        return ans