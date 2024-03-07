class Solution:
    def digitSum(self, s: str, k: int) -> str:
        if len(s) <= k:
            return s
        while len(s) > k:
            ans = ""
            sNum = []
            for i in s:
                sNum.append(int(i))
            for i in range(0, len(s), k):
                if i+k >= len(s):
                    ans += str(sum(sNum[i:]))
                else:
                    print(sNum[i:i+k])
                    ans += str(sum(sNum[i:i+k]))
            s = ans
        return ans