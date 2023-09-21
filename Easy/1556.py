"""class Solution:
    def thousandSeparator(self, n: int) -> str:
        n = str(n)
        res = ""
        dot = 4

        for i in range(1,len(n)+1):
            if i == dot:
                res = n[-i] + "." + res
                dot+=3
            else:
                res = n[-i] + res
            print(i, res)
        return res"""

class Solution:
    def thousandSeparator(self, n: int) -> str:
        if n == 0:
            return "0"
        ans = ""
        count = 0
        while n > 0:
            print(n,count)
            if count == 0:
                ans += str(n%10)
            elif count%3 == 0:
                ans += "."
                ans += str(n%10)
            else:
                ans += str(n%10)
            n = n//10
            count += 1
            print(ans)
            
        return (ans[::-1])