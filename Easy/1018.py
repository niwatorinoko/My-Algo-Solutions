class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        ans = []
        num = ""
        for i in nums:
            num += str(i)
            if int(num, 2)%5 == 0:
                ans.append(True)
            else:
                ans.append(False)
        return ans