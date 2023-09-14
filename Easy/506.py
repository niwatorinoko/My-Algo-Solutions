class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sortedscore = newlist = sorted(score, reverse=True)
        ans = []
        for i in score:
            prize = sortedscore.index(i)
            if prize == 0:
                ans.append("Gold Medal")
            elif prize == 1:
                ans.append("Silver Medal")
            elif prize == 2:
                ans.append("Bronze Medal")
            else:
                ans.append(str(prize+1))

        return ans