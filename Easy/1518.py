class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        def exchange(bottles, exchange):
            return bottles//exchange + bottles%exchange
        ans = numBottles
        while numBottles >= numExchange:
            ans += numBottles//numExchange
            numBottles = exchange(numBottles, numExchange)
        return ans