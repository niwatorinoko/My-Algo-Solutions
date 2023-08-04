class Solution:
    def findComplement(self, num: int) -> int:
        n = ""
        for i in bin(num)[2:]:
            if i == "0":
                n += "1"
            else:
                n += "0"
        return int(n, 2)