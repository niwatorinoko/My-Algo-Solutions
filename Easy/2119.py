class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if num == 0:
            return True
        if str(num)[-1] == "0":
            return False
        return True