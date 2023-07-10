class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        while len(nums) != 1:
            temp = []
            minOrmax = True
            for i in range(0, len(nums), 2):
                if minOrmax == True:
                    temp.append(min(nums[i], nums[i+1]))
                    minOrmax = False
                else:
                    temp.append(max(nums[i], nums[i+1]))
                    minOrmax = True
            nums = temp
        return nums[0]