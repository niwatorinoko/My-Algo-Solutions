class Solution:
    def addDigits(self, num: int) -> int:
        res = str(num)
        while len(res) >= 2:
            n = 0
            for i in res:
                n += int(i)
            res = str(n)
        return int(res)