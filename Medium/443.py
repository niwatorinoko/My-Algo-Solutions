class Solution:
    def compress(self, chars: List[str]) -> int:
        cur = chars[0]
        count = 1
        ans = []
        for i in range(1, len(chars)):
            print(ans,count)
            if chars[i] == cur:
                count += 1
            else:
                if count > 1:
                    ans.append(cur)
                    for j in str(count):
                        ans.append(j)
                else:
                    ans.append(cur)
                cur = chars[i]
                count = 1
        if count > 1:
            ans.append(cur)
            for j in str(count):
                ans.append(j)
        else:
            ans.append(cur)
        for i in range(len(ans)):
            chars[i] = ans[i]
        return len(ans)