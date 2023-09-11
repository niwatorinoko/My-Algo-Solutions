class Solution:
    def check(self, nums: List[int]) -> bool:
        sortedarr = sorted(nums)
        for i in range(len(nums)):
            temp = sortedarr[i:] + sortedarr[:i]
            if nums == temp:
                return True

        return False