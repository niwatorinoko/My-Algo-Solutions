class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        if len(cost) <= 2:
            return sum(cost)
        ans = 0
        cost.sort(reverse=True)
        for i in range(0, len(cost), 3):
            if len(cost) < i+2:
                ans += cost[i]
                break
            if len(cost) < i+1:
                break
            ans += cost[i] + cost[i+1]
        return ans