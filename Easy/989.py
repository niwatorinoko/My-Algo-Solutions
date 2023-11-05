class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        n = 0
        for i in num:
            n = 10*n + i
        ans = n+k
        ans_li = []
        while ans>0:
            ans_li = [ans%10]+ans_li
            ans = ans//10
        return ans_li