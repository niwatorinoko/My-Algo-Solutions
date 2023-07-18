class Solution:
    def reverse(self, x: int) -> int:
        str_x = str(x)
        temp = ""
        if x >= 0:
            for i in range(len(str_x)):
                temp = str_x[i] + temp
        else:
            for i in range(1, len(str_x)):
                temp = str_x[i] + temp
            temp = "-" + temp
        
        if int(temp) < -2**31 or int(temp) > 2**(31)-1:
            return 0
        return int(temp)

