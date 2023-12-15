class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        total_distinct = len(set(nums)) #必要な要素数
        counts = Counter()
        ans = 0
        left = 0

        for right in range(len(nums)):
            #nums[right]のvalueに１足す
            counts[nums[right]] += 1
            

            # 現在のウィンドウが完全であるかチェック
            while len(counts) == total_distinct:
                ans += len(nums) - right
                counts[nums[left]] -= 1
                if counts[nums[left]] == 0:
                    del counts[nums[left]]
                left += 1

        return ans