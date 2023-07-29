class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        binary = ""
        while n != 0:
            binary = str(n%2) + binary
            n = n//2
        ans = ""
        for i in binary:
            if i== "0":
                ans = ans + "1"
            elif i == "1":
                ans = ans + "0"
        res = 0
        j = 0
        for i in range(len(ans)-1, -1, -1):
            res += int(ans[j])*(2**i)
            j += 1
        return res