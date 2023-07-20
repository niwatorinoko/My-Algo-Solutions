class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        ans = []
        count = Counter(dict(nums1))+Counter(dict(nums2))
        for i, j in sorted(count.items()):
            ans.append([i,j])
        return ans