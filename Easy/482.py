class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace("-","").upper()
        head = len(s)%k
        ans = []
        if head>0:
            ans.append(s[:head])
        for i in range(head, len(s), k):
            ans.append(s[i:i+k])
        return "-".join(ans)