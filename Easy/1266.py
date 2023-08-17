class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        pos = points[0]
        time = 0
        for i in range(1,len(points)):
            while pos != points[i]:
                if pos[0] < points[i][0]:
                    pos[0] += 1
                if pos[0] > points[i][0]:
                    pos[0] -= 1
                if pos[1] < points[i][1]:
                    pos[1] += 1
                if pos[1] > points[i][1]:
                    pos[1] -= 1
                time += 1
        return time