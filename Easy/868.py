class Solution:
    def binaryGap(self, n: int) -> int:
        n_bin = bin(n)[2:]
        if n_bin.count("1") <= 1:
            return 0
        ans = 0
        count = 0
        for i in n_bin:
            if i == "0":
                count += 1
            else:
                ans = max(ans, count+1)
                count = 0
        return ans