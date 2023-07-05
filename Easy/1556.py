class Solution:
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
        return res