class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans = [0]*len(arr)
        maxx = -1
        for i in range(len(arr)-1, -1, -1):
            ans[i] = maxx
            maxx = max(maxx, arr[i])
        return ans