class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        ans = []
        for i in range(0, len(s), k):
            ans.append(s[i:i+k])
        ans[-1] += (-len(s)%k)*(fill)
        return ans