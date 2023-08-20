class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        for i in suits:
            if i != suits[0]:
                break
        else:
            return "Flush"
        
        ranksCounter = sorted(Counter(ranks).values())

        for i in reversed(ranksCounter):
            if i>=3:
                return "Three of a Kind"
            elif i == 2:
                return "Pair"
        return "High Card"