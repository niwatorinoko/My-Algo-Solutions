class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        def check(temp,k):
            for j in range(1, k+1):
                if j not in temp:
                    return False
            return True

        for i in range(k, len(nums)+1):
            temp = nums[-i:]
            if check(temp,k):
                return i