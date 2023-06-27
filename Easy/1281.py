class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        sum_di = 0
        for i in str(n):
            product *= int(i)
            sum_di += int(i)
        return product - sum_di