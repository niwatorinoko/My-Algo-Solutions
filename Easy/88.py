class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p2 = 0
        for i in range(n):
            nums1.append(nums2[p2])
            p2 += 1
            nums1.remove(0)

        nums1.sort()