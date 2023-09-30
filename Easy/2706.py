class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        if sum(sorted(prices)[:2]) <= money:
            return money-sum(sorted(prices)[:2])
        return money