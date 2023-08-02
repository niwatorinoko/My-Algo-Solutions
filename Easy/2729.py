class Solution:
    def isFascinating(self, n: int) -> bool:
        num = str(n) + str(2*n) + str(3*n)
        numCount = Counter(num)
        if sorted(numCount.keys()) != ["1","2","3","4","5","6","7","8","9"]:
            return False
        if max(numCount.values()) >= 2:
            return False
        return True