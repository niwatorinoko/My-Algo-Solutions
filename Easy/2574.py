class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        ans = []
        leftSum = [0]
        rightSum = [0]

        for i in range(1, len(nums)):
            leftSum.append(sum(nums[:i]))
            rightSum.append(sum(nums[-i:]))

        rightSum.reverse()

        for i in range(len(nums)):
            ans.append(abs(leftSum[i] - rightSum[i]))

        return ans