class Solution:
    def totalMoney(self, n: int) -> int:
        ans = 0
        lastweek = [1]
        lastmon = 1
        for i in range(1, n):
            if i%7 == 0:
                ans += sum(lastweek)
                lastmon = lastweek[0]+1
                lastweek = [lastmon]
            else:
                lastweek.append(lastweek[-1]+1)
        ans += sum(lastweek)
        return ans
