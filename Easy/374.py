# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        if guess(n) == 0:
            return n
        l, r = 0, n
        for i in range(n):
            #print(l,r)
            if guess((l+r)//2) == 0:
                return (l+r)//2
            elif guess((l+r)//2) == 1:
                l = (l+r)//2
            else:
                r = (l+r)//2
        return 0