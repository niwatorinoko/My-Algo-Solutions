# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n
        while l <= r:
            if isBadVersion((l+r)//2):
                r = (l+r)//2
            else:
                if isBadVersion((l+r)//2) == False:
                    l = (l+r)//2
            if isBadVersion(l):
                return l
            else:
                l += 1
        else:
            return 0