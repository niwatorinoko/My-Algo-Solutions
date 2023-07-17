class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        res = 0
        count = collections.Counter(nums)
        for i in count.keys():
            if count[i] == 1:
                res += i
        return res