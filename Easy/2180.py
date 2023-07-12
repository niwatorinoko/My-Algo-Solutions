class Solution:
    def countEven(self, num: int) -> int:
        res = 0
        for i in range(1, num+1):
            temp = 0
            for j in str(i):
                temp += int(j)
            if temp % 2 == 0:
                res += 1
        return res