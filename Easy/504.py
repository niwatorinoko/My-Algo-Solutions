class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        ans = ""
        flag = True
        if num < 0:
            flag = False
        num = abs(num)
        while num > 0:
            ans = str(num%7) + ans
            num = num//7
        if num > 0:
            ans = str(num) + ans
        if flag:
            return ans
        return "-" + ans