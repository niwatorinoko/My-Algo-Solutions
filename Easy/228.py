class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        ans = []
        cur = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i]-1 != cur[-1]:
                if len(cur) == 1:
                    ans.append(str(cur[0]))
                    cur = [nums[i]]
                elif len(cur) >= 2:
                    ans.append(str(cur[0]) + "->" + str(cur[-1]))
                    cur = [nums[i]]
            else:
                cur.append(nums[i])

        if len(cur) == 1:
            ans.append(str(cur[0]))
        elif len(cur) >= 2:
            ans.append(str(cur[0]) + "->" + str(cur[-1]))
            
        return ans