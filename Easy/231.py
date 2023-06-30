class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        if n == 1:
            return True
        i = 1
        while 2**(i)<=n:
            if 2**(i) == n:
                return True
            i += 1
        return False