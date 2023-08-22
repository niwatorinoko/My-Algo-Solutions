class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if high == low:
            if high%2 == 1:
                return 1
        if low%2 == 1 and high%2 == 1:
            return (high - low )//2 + 1
        if low%2 == 0 and high%2 == 0:
            return (high - low)//2
        return (high-low)//2+1