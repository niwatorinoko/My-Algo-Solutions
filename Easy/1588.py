class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        ans = 0
        k = 1
        for i in range(len(arr)):
            for j in range(k, len(arr)+1):
                if len(arr[i:j]) % 2 != 0:
                    ans += sum(arr[i:j])
            k += 1
        return ans