class Solution:
    def arrangeCoins(self, n: int) -> int:
        k = 1
        while True:
            if n == k:
                return k
            elif n > k:
                n -= k
                k += 1
            else:
                return k-1