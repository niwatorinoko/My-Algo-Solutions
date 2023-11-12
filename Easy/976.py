class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        # 数値リストを逆順にソート
        nums.sort(reverse=True)

        # 隣接する3つの数値で三角形を形成できるかチェック
        for i in range(len(nums) - 2):
            if nums[i] < nums[i + 1] + nums[i + 2]:
                # 三角形が形成できれば、その周長を返す
                return nums[i] + nums[i + 1] + nums[i + 2]

        # 三角形を形成できない場合は0を返す
        return 0
