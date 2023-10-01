class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        a = 1
        b = n-a
        def isNoZero(n1, n2):
            if "0" not in str(n1):
                if "0" not in str(n2):
                    return True
            return False
        
        for i in range(1, n):
            if isNoZero(a,b):
                return [a,b]
            a = i
            b = n-a