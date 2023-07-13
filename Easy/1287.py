class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        for i in set(arr):
            if arr.count(i) / len(arr) > 0.25:
                return i