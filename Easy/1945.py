class Solution:
    def getLucky(self, s: str, k: int) -> int:
        ans = ""
        for i in s:
            ans += str(ord(i)-96)
        for i in range(k):
            temp = 0
            for j in ans:
                temp += int(j)
            ans = str(temp)
        return int(ans)