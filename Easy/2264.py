class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ans = ""
        for i in range(len(num)-2):
            if len(set(num[i:i+3])) == 1:
                if ans < num[i:i+3]:
                    ans = num[i:i+3]
        return ans