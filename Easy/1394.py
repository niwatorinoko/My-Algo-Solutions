class Solution:
    def findLucky(self, arr: List[int]) -> int:
        ans = -1
        for i,j in Counter(arr).items():
            if i == j:
                if ans < i:
                    ans = i
        return ans