class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        n = 1
        while n*n < num:
            n += 1
        if n*n == num:
            return True
        return False