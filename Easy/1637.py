class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        ans = 0
        onlyX=[]
        for i in range(len(points)):
            onlyX.append(points[i][0])
        onlyX = sorted(onlyX)
        for i in range(1,len(onlyX)):
            ans = max(abs(onlyX[i]-onlyX[i-1]),ans)
        return ans