class Solution:
    def pivotInteger(self, n: int) -> int:
        numli = []
        for i in range(n):
            numli.append(i+1)
        for i in range(n):
            l = sum(numli[:i+1])
            r = sum(numli[i:])
            if l == r:
                return i+1
        return -1